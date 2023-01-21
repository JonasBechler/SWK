import shutil
from pathlib import Path


def main():
    main_config = Path.cwd() / "main_config.json"

    handyticket_config = Path.cwd() / "SWK_Handyticket" / "config.json"
    konrad_config = Path.cwd() / "SWK_Konrad" / "config.json"
    login_config = Path.cwd() / "SWK_Login" / "config.json"
    native_config = Path.cwd() / "SWK_Native" / "config.json"


    shutil.copyfile(main_config, handyticket_config)
    shutil.copyfile(main_config, konrad_config)
    shutil.copyfile(main_config, login_config)
    shutil.copyfile(main_config, native_config)

if __name__ == "__main__":
    main()