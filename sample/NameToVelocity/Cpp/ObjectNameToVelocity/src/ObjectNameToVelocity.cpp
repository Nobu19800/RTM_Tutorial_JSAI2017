// -*- C++ -*-
/*!
 * @file  ObjectNameToVelocity.cpp
 * @brief 与えられた文字列をTimedVelocity2Dへ変換
 * @date $Date$
 *
 * $Id$
 */

#include "ObjectNameToVelocity.h"

// Module specification
// <rtc-template block="module_spec">
static const char* objectnametovelocity_spec[] =
  {
    "implementation_id", "ObjectNameToVelocity",
    "type_name",         "ObjectNameToVelocity",
    "description",       "与えられた文字列をTimedVelocity2Dへ変換",
    "version",           "1.0.0",
    "vendor",            "AIST",
    "category",          "Converte",
    "activity_type",     "PERIODIC",
    "kind",              "DataFlowComponent",
    "max_instance",      "1",
    "language",          "C++",
    "lang_type",         "compile",
    ""
  };
  // </rtc-template>

  /*!
   * @brief constructor
   * @param manager Maneger Object
   */
  ObjectNameToVelocity::ObjectNameToVelocity(RTC::Manager* manager)
	  // <rtc-template block="initializer">
	  : RTC::DataFlowComponentBase(manager),
	  m_inStringDataIn("inStringData", m_inStringData),
	  m_outVelocityDataOut("outVelocityData", m_outVelocityData)

	  // </rtc-template>
  {
  }

  /*!
   * @brief destructor
   */
ObjectNameToVelocity::~ObjectNameToVelocity()
{
}



RTC::ReturnCode_t ObjectNameToVelocity::onInitialize()
{
	// Registration: InPort/OutPort/Service
	// <rtc-template block="registration">
	// Set InPort buffers
	addInPort("inStringData", m_inStringDataIn);

	// Set OutPort buffer
	addOutPort("outVelocityData", m_outVelocityDataOut);

	// Set service provider to Ports

	// Set service consumers to Ports

	// Set CORBA Service Ports

	// </rtc-template>

	// <rtc-template block="bind_config">
	// </rtc-template>

	return RTC::RTC_OK;
}

/*
RTC::ReturnCode_t ObjectNameToVelocity::onFinalize()
{
return RTC::RTC_OK;
}
*/

/*
RTC::ReturnCode_t ObjectNameToVelocity::onStartup(RTC::UniqueId ec_id)
{
return RTC::RTC_OK;
}
*/

/*
RTC::ReturnCode_t ObjectNameToVelocity::onShutdown(RTC::UniqueId ec_id)
{
return RTC::RTC_OK;
}
*/


RTC::ReturnCode_t ObjectNameToVelocity::onActivated(RTC::UniqueId ec_id)
{
	//出力データを初期化しておく
	m_outVelocityData.data.vx = 0;
	m_outVelocityData.data.vy = 0;
	m_outVelocityData.data.va = 0;

	m_outVelocityDataOut.write();

	return RTC::RTC_OK;
}


RTC::ReturnCode_t ObjectNameToVelocity::onDeactivated(RTC::UniqueId ec_id)
{
	//停止させるために出力データを初期化
	m_outVelocityData.data.vx = 0;
	m_outVelocityData.data.vy = 0;
	m_outVelocityData.data.va = 0;

	m_outVelocityDataOut.write();

	return RTC::RTC_OK;
}


RTC::ReturnCode_t ObjectNameToVelocity::onExecute(RTC::UniqueId ec_id)
{

	if (m_inStringDataIn.isNew())
	{
		//入力文字列の読み込み
		m_inStringDataIn.read();

		//入力文字列の判定により、対象文字列の場合にvxの値を操作する
		if (strcmp(m_inStringData.data, "bow tie") == 0)
		{
			m_outVelocityData.data.vx = 0.5;
		}
		else if (strcmp(m_inStringData.data, "hook") == 0)
		{
			m_outVelocityData.data.vx = -0.5;
		}
		else if (strcmp(m_inStringData.data, "pinwheel") == 0)
		{
			m_outVelocityData.data.va = 0.1;
		}
		else if (strcmp(m_inStringData.data, "envelope") == 0)
		{
			m_outVelocityData.data.va = -0.1;
		}
		else
		{
			m_outVelocityData.data.vx = 0;  //対象外文字列の場合初期化
		}
		  //出力用データを書き込む
		  m_outVelocityDataOut.write();
	   }

  return RTC::RTC_OK;
}


RTC::ReturnCode_t ObjectNameToVelocity::onAborting(RTC::UniqueId ec_id)
{
  return RTC::RTC_OK;
}


RTC::ReturnCode_t ObjectNameToVelocity::onError(RTC::UniqueId ec_id)
{
  return RTC::RTC_OK;
}


RTC::ReturnCode_t ObjectNameToVelocity::onReset(RTC::UniqueId ec_id)
{
  return RTC::RTC_OK;
}

/*
RTC::ReturnCode_t ObjectNameToVelocity::onStateUpdate(RTC::UniqueId ec_id)
{
  return RTC::RTC_OK;
}
*/

/*
RTC::ReturnCode_t ObjectNameToVelocity::onRateChanged(RTC::UniqueId ec_id)
{
  return RTC::RTC_OK;
}
*/



extern "C"
{
 
  void ObjectNameToVelocityInit(RTC::Manager* manager)
  {
    coil::Properties profile(objectnametovelocity_spec);
    manager->registerFactory(profile,
                             RTC::Create<ObjectNameToVelocity>,
                             RTC::Delete<ObjectNameToVelocity>);
  }
  
};


