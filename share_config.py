import shutil
from pathlib import Path


def main():
    main_config = Path.cwd() / "main_config.json"

    handyticket_config = Path.cwd() / "SWK_Handyticket" / "config.json"
    handyticket_react_config = Path.cwd() / "SWK_Handyticket"/ "SWK_Handyticket_React" / "src" /  "config.json"

    konrad_config = Path.cwd() / "SWK_Konrad" / "config.json"
    konrad_react_config = Path.cwd() / "SWK_Konrad" / "SWK_Konrad_React" / "src" / "config.json"

    login_config = Path.cwd() / "SWK_Login" / "config.json"
    login_react_config = Path.cwd() / "SWK_Login" / "SWK_Login_React" / "src" / "config.json"

    native_config = Path.cwd() / "SWK_Native" / "config.json"


    shutil.copyfile(main_config, handyticket_config)
    shutil.copyfile(main_config, handyticket_react_config)

    shutil.copyfile(main_config, konrad_config)
    shutil.copyfile(main_config, konrad_react_config)
    
    shutil.copyfile(main_config, login_config)
    shutil.copyfile(main_config, login_react_config)

    shutil.copyfile(main_config, native_config)

if __name__ == "__main__":
    main()