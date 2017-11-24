#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Python -*-

"""
 @file ObjectNameToVelocity.py
 @brief ModuleDescription
 @date $Date$


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
objectnametovelocity_spec = ["implementation_id", "ObjectNameToVelocity", 
		 "type_name",         "ObjectNameToVelocity", 
		 "description",       "ModuleDescription", 
		 "version",           "1.0.0", 
		 "vendor",            "AIST", 
		 "category",          "Convert", 
		 "activity_type",     "STATIC", 
		 "max_instance",      "1", 
		 "language",          "Python", 
		 "lang_type",         "SCRIPT",
		 ""]
# </rtc-template>

##
# @class ObjectNameToVelocity
# @brief ModuleDescription
# 
# 
class ObjectNameToVelocity(OpenRTM_aist.DataFlowComponentBase):
	
	##
	# @brief constructor
	# @param manager Maneger Object
	# 
	def __init__(self, manager):
		OpenRTM_aist.DataFlowComponentBase.__init__(self, manager)

		self._d_inDataString = RTC.TimedString(RTC.Time(0,0), [])
		"""
		"""
		self._inDataStringIn = OpenRTM_aist.InPort("inDataString", self._d_inDataString)
		

		self._d_outDataVelocity = RTC.TimedVelocity2D(RTC.Time(0,0), RTC.Velocity2D(0,0,0))
		"""
		"""
		self._outDataVelocityOut = OpenRTM_aist.OutPort("outDataVelocity", self._d_outDataVelocity)


		


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
		self.addInPort("inDataString",self._inDataStringIn)
		
		# Set OutPort buffers
		self.addOutPort("outDataVelocity",self._outDataVelocityOut)
		
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
		
		self._d_outDataVelocity.data.vx = 0.0
		self._d_outDataVelocity.data.vy = 0.0
		self._d_outDataVelocity.data.va = 0.0

		self._outDataVelocityOut.write()

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
		
		self._d_outDataVelocity.data.vx = 0.0
		self._d_outDataVelocity.data.vy = 0.0
		self._d_outDataVelocity.data.va = 0.0

		self._outDataVelocityOut.write()

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
	    
		# 特定の文字列で、前進と後退などを行う
		if self._inDataStringIn.isNew():

			data = self._inDataStringIn.read()

			if data.data == "bow tie":
			
				self._d_outDataVelocity.data.vx = 0.5
			
			elif data.data == "hook":
			
				self._d_outDataVelocity.data.vx = -0.5

			elif data.data == "pinwheel":

				self._d_outDataVelocity.data.va = 0.1

			elif data.data == "envelope":

				self._d_outDataVelocity.data.va = -0.1

			else:

				self._d_outDataVelocity.data.vx = 0
				self._d_outDataVelocity.data.vy = 0
				self._d_outDataVelocity.data.va = 0

			self._outDataVelocityOut.write()
		
		return RTC.RTC_OK
	
		##
		#
		# The aborting action when main logic error occurred.
		# former rtc_aborting_entry()
		#
		# @param ec_id target ExecutionContext Id
		#
		# @return RTC::ReturnCode_t
		#
		#
	def onAborting(self, ec_id):
	
		return RTC.RTC_OK
	
		##
		#
		# The error action in ERROR state
		# former rtc_error_do()
		#
		# @param ec_id target ExecutionContext Id
		#
		# @return RTC::ReturnCode_t
		#
		#
	def onError(self, ec_id):
	
		return RTC.RTC_OK
	
		##
		#
		# The reset action that is invoked resetting
		# This is same but different the former rtc_init_entry()
		#
		# @param ec_id target ExecutionContext Id
		#
		# @return RTC::ReturnCode_t
		#
		#
	def onReset(self, ec_id):
	
		return RTC.RTC_OK
	
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
	



def ObjectNameToVelocityInit(manager):
    profile = OpenRTM_aist.Properties(defaults_str=objectnametovelocity_spec)
    manager.registerFactory(profile,
                            ObjectNameToVelocity,
                            OpenRTM_aist.Delete)

def MyModuleInit(manager):
    ObjectNameToVelocityInit(manager)

    # Create a component
    comp = manager.createComponent("ObjectNameToVelocity")

def main():
	mgr = OpenRTM_aist.Manager.init(sys.argv)
	mgr.setModuleInitProc(MyModuleInit)
	mgr.activateManager()
	mgr.runManager()

if __name__ == "__main__":
	main()

