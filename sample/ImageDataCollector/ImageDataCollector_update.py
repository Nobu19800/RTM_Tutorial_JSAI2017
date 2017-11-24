#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Python -*-

"""
 @file ImageDataCollector.py
 @brief Collects sensor data from camera image
 @date $Date$


"""
import sys
import os

# Import RTM module
import RTC
import OpenRTM_aist

import cv2
import numpy as np
from datetime import datetime as dt

sys.path.append(".")

# Import Service implementation class
# <rtc-template block="service_impl">

# </rtc-template>

# Import Service stub modules
# <rtc-template block="consumer_import">
# </rtc-template>


# This module's spesification
# <rtc-template block="module_spec">
imagedatacollector_spec = [
    "implementation_id", "ImageDataCollector",
    "type_name", "ImageDataCollector",
    "description", "Collects sensor data from camera image",
    "version", "1.0.0",
    "vendor", "takahasi",
    "category", "Collector",
    "activity_type", "STATIC",
    "max_instance", "1",
    "language", "Python",
    "lang_type", "SCRIPT",
    ""
]
# </rtc-template>


##
# @class ImageDataCollector
# @brief Collects sensor data from camera image
#
#
class ImageDataCollector(OpenRTM_aist.DataFlowComponentBase):
    ##
    # @brief constructor
    # @param manager Maneger Object
    #
    def __init__(self, manager):
        OpenRTM_aist.DataFlowComponentBase.__init__(self, manager)

        self._d_image = RTC.CameraImage(RTC.Time(0, 0), 0, 0, 0, [], 0, [])
        self._imageIn = OpenRTM_aist.InPort("image", self._d_image)

        self._d_sensor = RTC.TimedShortSeq(RTC.Time(0, 0), [])
        self._sensorIn = OpenRTM_aist.InPort("sensor", self._d_sensor)
        # initialize of configuration-data.
        # <rtc-template block="init_conf_param">

        # </rtc-template>


    ##
    #
    # The initialize action (on CREATED->ALIVE transition)
    # formaer rtc_init_entry()
    #
    # @return RTC::ReturnCode_t
    #
    #
    def onInitialize(self):
        # Bind variables and configuration variable

        # Set InPort buffers
        self.addInPort("image", self._imageIn)
        self.addInPort("sensor", self._sensorIn)

        # Set OutPort buffers

        # Set service provider to Ports

        # Set service consumers to Ports

        # Set CORBA Service Ports

        return RTC.RTC_OK

    #   ##
    #   #
    #   # The finalize action (on ALIVE->END transition)
    #   # formaer rtc_exiting_entry()
    #   #
    #   # @return RTC::ReturnCode_t
    #
    #   #
    # def onFinalize(self):
    #
    #   return RTC.RTC_OK

    #   ##
    #   #
    #   # The startup action when ExecutionContext startup
    #   # former rtc_starting_entry()
    #   #
    #   # @param ec_id target ExecutionContext Id
    #   #
    #   # @return RTC::ReturnCode_t
    #   #
    #   #
    # def onStartup(self, ec_id):
    #
    #   return RTC.RTC_OK

    #   ##
    #   #
    #   # The shutdown action when ExecutionContext stop
    #   # former rtc_stopping_entry()
    #   #
    #   # @param ec_id target ExecutionContext Id
    #   #
    #   # @return RTC::ReturnCode_t
    #   #
    #   #
    # def onShutdown(self, ec_id):
    #
    #   return RTC.RTC_OK

    ##
    #
    # The activated action (Active state entry action)
    # former rtc_active_entry()
    #
    # @param ec_id target ExecutionContext Id
    #
    # @return RTC::ReturnCode_t
    #
    #
    def onActivated(self, ec_id):
        # 変数の初期化
        self._count = 0
        t = dt.now()

        # センサ用出力ディレクトリ作成
        self._image_dir = "image_" + t.strftime('%Y%m%d')
        if not os.path.exists(self._image_dir):
            os.mkdir(self._image_dir)

        # センサ用出力ディレクトリ作成
        self._sensor_dir = "sensor_" + t.strftime('%Y%m%d')
        if not os.path.exists(self._sensor_dir):
            os.mkdir(self._sensor_dir)

        self._f = open(self._sensor_dir + "/sensor.csv", 'w')

        return RTC.RTC_OK

    ##
    #
    # The deactivated action (Active state exit action)
    # former rtc_active_exit()
    #
    # @param ec_id target ExecutionContext Id
    #
    # @return RTC::ReturnCode_t
    #
    #
    def onDeactivated(self, ec_id):

        self._count = 0
        self._f.close()

        return RTC.RTC_OK

    ##
    #
    # The execution action that is invoked periodically
    # former rtc_active_do()
    #
    # @param ec_id target ExecutionContext Id
    #
    # @return RTC::ReturnCode_t
    #
    #
    def onExecute(self, ec_id):

        # 変数の初期化
        self._count = 0
        t = dt.now()
        
        # センサ用出力ディレクトリ作成
        self._image_dir = "image_" + t.strftime('%Y%m%d')
        if not os.path.exists(self._image_dir):
            os.mkdir(self._image_dir)
        
        # センサ用出力ディレクトリ作成
        self._sensor_dir = "sensor_" + t.strftime('%Y%m%d')
        if not os.path.exists(self._sensor_dir):
            os.mkdir(self._sensor_dir)
        
        return RTC.RTC_OK

    def onExecute(self, ec_id):
        if self._imageIn.isNew():
            # 画像イメージの変換
            data = self._imageIn.read()
            frame = np.frombuffer(data.pixels, dtype=np.uint8)
            frame = frame.reshape(data.height, data.width, 3)
            
            # 画像イメージの保存
            cv2.imwrite(self._image_dir + "/" + str(self._count) + ".png", frame)
            self._count += 1
            
        if self._sensorIn.isNew():
            # センサデータの保存
            data = self._sensorIn.read()
            self._f.write(",".join(map(str, data.data)) + "\n")

        return RTC.RTC_OK

    #   ##
    #   #
    #   # The aborting action when main logic error occurred.
    #   # former rtc_aborting_entry()
    #   #
    #   # @param ec_id target ExecutionContext Id
    #   #
    #   # @return RTC::ReturnCode_t
    #   #
    #   #
    # def onAborting(self, ec_id):
    #
    #   return RTC.RTC_OK

    #   ##
    #   #
    #   # The error action in ERROR state
    #   # former rtc_error_do()
    #   #
    #   # @param ec_id target ExecutionContext Id
    #   #
    #   # @return RTC::ReturnCode_t
    #   #
    #   #
    # def onError(self, ec_id):
    #
    #   return RTC.RTC_OK

    #   ##
    #   #
    #   # The reset action that is invoked resetting
    #   # This is same but different the former rtc_init_entry()
    #   #
    #   # @param ec_id target ExecutionContext Id
    #   #
    #   # @return RTC::ReturnCode_t
    #   #
    #   #
    # def onReset(self, ec_id):
    #
    #   return RTC.RTC_OK

    #   ##
    #   #
    #   # The state update action that is invoked after onExecute() action
    #   # no corresponding operation exists in OpenRTm-aist-0.2.0
    #   #
    #   # @param ec_id target ExecutionContext Id
    #   #
    #   # @return RTC::ReturnCode_t
    #   #

    #   #
    # def onStateUpdate(self, ec_id):
    #
    #   return RTC.RTC_OK

    #   ##
    #   #
    #   # The action that is invoked when execution context's rate is changed
    #   # no corresponding operation exists in OpenRTm-aist-0.2.0
    #   #
    #   # @param ec_id target ExecutionContext Id
    #   #
    #   # @return RTC::ReturnCode_t
    #   #
    #   #
    # def onRateChanged(self, ec_id):
    #
    #   return RTC.RTC_OK


def ImageDataCollectorInit(manager):
    profile = OpenRTM_aist.Properties(defaults_str=imagedatacollector_spec)
    manager.registerFactory(profile,
                            ImageDataCollector,
                            OpenRTM_aist.Delete)


def MyModuleInit(manager):
    ImageDataCollectorInit(manager)

    # Create a component
    manager.createComponent("ImageDataCollector")


def main():
    mgr = OpenRTM_aist.Manager.init(sys.argv)
    mgr.setModuleInitProc(MyModuleInit)
    mgr.activateManager()
    mgr.runManager()

if __name__ == "__main__":
    main()
