# This is a sample Python script.
import NormalLine_create
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import SWH_config
import SWH_create

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    config = SWH_config.SwhConfig(f"./config/swhPinLayout.json")

    dxf_swh = SWH_create.SwhCreate(config)
    # dxf_line = NormalLine_create.NormalLineCreate(config, dxf_swh)

    dxf_swh.save_as(f"./result/SWH_create2.dxf")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
