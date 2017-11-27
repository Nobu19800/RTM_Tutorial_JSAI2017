#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Python -*-

"""
 @file RobotController.py
 @brief Robot Controller Component
 @date $Date$

 @author 宮本　信彦　n-miyamoto@aist.go.jp
 産業技術総合研究所　ロボットイノベーション研究センター
 ロボットソフトウエアプラットフォーム研究チーム

"""
import sys
import time
sys.path.append(".")

# Import RTM module
import RTC
import OpenRTM_aist


# Import Service implementation class
# <rtc-template block="service_impl">

# </rtc-template>

# Import Service stub modules
# <rtc-template block="consumer_import">
# </rtc-template>


# This module's spesification
# <rtc-template block="module_spec">
robotcontroller_spec = ["implementation_id", "RobotController", 
		 "type_name",         "RobotController", 
		 "description",       "Robot Controller Component", 
		 "version",           "1.0.0", 
		 "vendor",            "AIST", 
		 "category",          "Controller", 
		 "activity_type",     "STATIC", 
		 "max_instance",      "1", 
		 "language",          "Python", 
		 "lang_type",         "SCRIPT",
		 "conf.default.speed_x", "0.0",
		 "conf.default.speed_r", "0.0",
		 "conf.default.stop_d", "30",

		 "conf.__widget__.speed_x", "slider.0.01",
		 "conf.__widget__.speed_r", "slider.0.01",
		 "conf.__widget__.stop_d", "text",
		 "conf.__constraints__.speed_x", "-1.5<x<1.5",
		 "conf.__constraints__.speed_r", "-2.0<x<2.0",

         "conf.__type__.speed_x", "double",
         "conf.__type__.speed_r", "double",
         "conf.__type__.stop_d", "int",

		 ""]
# </rtc-template>

##
# @class RobotController
# @brief Robot Controller Component
# 
# 講習会用Raspberry Piマウス操作コンポーネント
# 
# 
class RobotController(OpenRTM_aist.DataFlowComponentBase):
	
	##
	# @brief constructor
	# @param manager Maneger Object
	# 
	def __init__(self, manager):
		OpenRTM_aist.DataFlowComponentBase.__init__(self, manager)

		#in_arg = [None] * ((len(RTC._d_TimedShortSeq) - 4) / 2)
		#self._d_in = RTC.TimedShortSeq(*in_arg)
		
		self._d_in = RTC.TimedShortSeq(RTC.Time(0,0),[])
		"""
		距離センサのデータを入力
		 - Type: RTC::TimedShortSeq
		 - Number: 4
		"""
		self._inIn = OpenRTM_aist.InPort("in", self._d_in)
		
		#out_arg = [None] * ((len(RTC._d_TimedVelocity2D) - 4) / 2)
		#self._d_out = RTC.TimedVelocity2D(*out_arg)
		
		self._d_out = RTC.TimedVelocity2D(RTC.Time(0,0),RTC.Velocity2D(0.0,0.0,0.0))
		"""
		目標速度出力
		 - Type: RTC::TimedVelocity2D
		 - Unit: m,rad
		"""
		self._outOut = OpenRTM_aist.OutPort("out", self._d_out)


		


		# initialize of configuration-data.
		# <rtc-template block="init_conf_param">
		"""
		速度の設定
		 - Name: speed_x speed_x
		 - DefaultValue: 0.0
		 - Unit: m/s
		 - Constraint: -1.5<x<1.5
		"""
		self._speed_x = [0.0]
		"""
		回転速度
		 - Name: speed_r speed_r
		 - DefaultValue: 0.0
		 - Unit: rad/s
		 - Constraint: -2.0<x<2.0
		"""
		self._speed_r = [0.0]
		"""
		停止状態に遷移するためのセンサの値
		 - Name: stop_d stop_d
		 - DefaultValue: 30
		"""
		self._stop_d = [30]
		
		# </rtc-template>
		#センサ値を一時格納する変数
		self.sensor_data = [0,0,0,0]


		 
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
		self.bindParameter("speed_x", self._speed_x, "0.0")
		self.bindParameter("speed_r", self._speed_r, "0.0")
		self.bindParameter("stop_d", self._stop_d, "30")
		
		# Set InPort buffers
		self.addInPort("in",self._inIn)
		
		# Set OutPort buffers
		self.addOutPort("out",self._outOut)
		
		# Set service provider to Ports
		
		# Set service consumers to Ports
		
		# Set CORBA Service Ports
		
		return RTC.RTC_OK
	
	#	##
	#	# 
	#	# The finalize action (on ALIVE->END transition)
	#	# formaer rtc_exiting_entry()
	#	# 
	#	# @return RTC::ReturnCode_t
	#
	#	# 
	#def onFinalize(self):
	#
	#	return RTC.RTC_OK
	
	#	##
	#	#
	#	# The startup action when ExecutionContext startup
	#	# former rtc_starting_entry()
	#	# 
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onStartup(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	#	##
	#	#
	#	# The shutdown action when ExecutionContext stop
	#	# former rtc_stopping_entry()
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onShutdown(self, ec_id):
	#
	#	return RTC.RTC_OK
	
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
		#センサ値初期化
		self.sensor_data = [0,0,0,0]
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
		#ロボットを停止する
		self._d_out.data.vx = 0
		self._d_out.data.va = 0
		self._outOut.write()
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
		#入力データの存在確認
		if self._inIn.isNew():
			data = self._inIn.read()
			#この時点で入力データがm_inに格納される
			#入力データを別変数に格納
			self.sensor_data = data.data[:]
		#前進するときのみ停止するかを判定
		if self._speed_x[0] > 0:
			for d in self.sensor_data:
				#センサ値が設定値以上か判定
				if d > self._stop_d[0]:
					#センサ値が設定値以上の場合は停止
					self._d_out.data.vx = 0
					self._d_out.data.va = 0
					self._outOut.write()
					return RTC.RTC_OK
				
		#設定値以上の値のセンサが無い場合はコンフィギュレーションパラメータの値で操作
		self._d_out.data.vx = self._speed_x[0]
		self._d_out.data.va = self._speed_r[0]
		self._outOut.write()
				
		return RTC.RTC_OK
	
	#	##
	#	#
	#	# The aborting action when main logic error occurred.
	#	# former rtc_aborting_entry()
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onAborting(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	#	##
	#	#
	#	# The error action in ERROR state
	#	# former rtc_error_do()
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onError(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	#	##
	#	#
	#	# The reset action that is invoked resetting
	#	# This is same but different the former rtc_init_entry()
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onReset(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	#	##
	#	#
	#	# The state update action that is invoked after onExecute() action
	#	# no corresponding operation exists in OpenRTm-aist-0.2.0
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#

	#	#
	#def onStateUpdate(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	#	##
	#	#
	#	# The action that is invoked when execution context's rate is changed
	#	# no corresponding operation exists in OpenRTm-aist-0.2.0
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onRateChanged(self, ec_id):
	#
	#	return RTC.RTC_OK
	



def RobotControllerInit(manager):
    profile = OpenRTM_aist.Properties(defaults_str=robotcontroller_spec)
    manager.registerFactory(profile,
                            RobotController,
                            OpenRTM_aist.Delete)

def MyModuleInit(manager):
    RobotControllerInit(manager)

    # Create a component
    comp = manager.createComponent("RobotController")

def main():
	mgr = OpenRTM_aist.Manager.init(sys.argv)
	mgr.setModuleInitProc(MyModuleInit)
	mgr.activateManager()
	mgr.runManager()

if __name__ == "__main__":
	main()

