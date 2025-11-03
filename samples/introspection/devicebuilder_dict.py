import logging
import os
import asyncio
from sgr_commhandler.device_builder import DeviceBuilder


logger = logging.getLogger(__name__)


# initialize WAGO device using dict as properties
async def main():
    eid_name = 'SGr_00_0014_0000_WAGO_SmartMeter_V0.3.xml'
    eid_properties = {
        'serial_port': 'COM3',
        'slave_id': '1'
    }
    eid_path = os.path.join('..', '..', 'eids', eid_name)

    try:
        # build device using local EID
        device = DeviceBuilder().eid_path(eid_path).properties(eid_properties).build()
    except Exception as e:
        logger.error('Error creating device', e)
        return

    # introspection of device frame
    device_frame = device.get_specification()
    logger.info(f'Device Name = {device_frame.device_name}')

    # introspection of functional profile
    fp_frame = device.get_functional_profile("CurrentAC").get_specification()
    logger.info(f'FP Name = {fp_frame.functional_profile.functional_profile_name}')

    # introspection of data point
    dp_frame = device.get_data_point(("CurrentAC", "CurrentACL1")).get_specification()
    logger.info(f'DP Name = {dp_frame.data_point.data_point_name}')


# entry point
if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    asyncio.run(main())
