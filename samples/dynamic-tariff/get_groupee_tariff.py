import logging
import os
import asyncio
import json
from sgr_commhandler.device_builder import DeviceBuilder


logger = logging.getLogger(__name__)


# get dynamic tariff of Groupe-e
async def main():
    eid_name = 'SGr_00_mmmm_dddd_DynamicTariff_GroupeE_V2.0.xml'
    eid_properties = {
        'tariff_name': 'vario'
    }
    eid_path = os.path.join('..', '..', 'eids', eid_name)

    try:
        # build device using local EID
        device = DeviceBuilder().eid_path(eid_path).properties(eid_properties).build()
    except Exception as e:
        logger.error('Error creating device', e)
        return

    try:
        # test device connection
        await device.connect_async()
    except Exception as e:
        logger.error('Error connecting', e)
        return

    # dynamic tariff requires query parameters in each request
    dynamic_request_parameters = {
        'start_timestamp': '2026-10-01T00:00:00+02:00',
        'end_timestamp': '2026-10-02T00:00:00+02:00'
    }
    try:
        # get the dynamic price data
        value = await device.get_data_point(('DynamicTariff', 'TariffSupply')).get_value_async(dynamic_request_parameters)
        logger.info(f'TariffSupply: {json.dumps(value)}')
    except Exception as e:
        logger.error('Error reading value', e)
    finally:
        await device.disconnect_async()
        logger.info('disconnected')


# entry point
if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    asyncio.run(main())
