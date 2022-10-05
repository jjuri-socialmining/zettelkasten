# Regression repo

```shell
git clone http://las-gitlab/hsc/regression.git
```
edit submodule info in `.git/config` from git protocol to http protocol.

from
```
[submodule "regression_common"]
        active = true
        url = http://las-gitlab/hsc/regression_common.git
```
to
```
[submodule "regression_common"]
        active = true
        url = http://las-gitlab/hsc/regression_common.git
```
Shell
```shell
cd regression
git submodule init
git submodule update
```

If You can not get api/fw by command, please do this manually
```
python -u make.py get_all --asics capellab ctcb lynx_400 --cplb_fw_version=CAPELLAB_NIGHTLY_1792 --cplb_api_version=CAPELLAB_NIGHTLY_1538 --ctcb_fw_version=CTCB_NIGHTLY_537 --ctcb_api_version=CTCB_NIGHTLY_1449 --lynx_400_fw_version=LYNX_NIGHTLY_132 --lynx_400_api_version=0.6.0.371
```

copy latest `hsc_api.pyd` and `hsc_api.py` to this directory
`regression\capella\api\lynx_400`

create/copy file version_json to capella folder like

```json
{"capellab": {"fw_arg": "cplb_fw_version", "api": "CAPELLAB_NIGHTLY_1536", "api_arg": "cplb_api_version", "fw": "CAPELLAB_NIGHTLY_1788", "asic_arg": "capellab"}, "capella": {"fw_arg": "cpl_fw_version", "api": "CAPELLA_NIGHTLY_1517", "api_arg": "cpl_api_version", "asic_arg": "capella", "fw": "CAPELLA_NIGHTLY_1757"}, "vega": {"fw_arg": "vega_fw_version", "api": "1.77.2135", "api_arg": "vega_api_version", "asic_arg": "vega", "fw": "VEGA_NIGHTLY_2366"}, "porrima": {"fw_arg": "por_fw_version", "api": "1.12.1155", "api_arg": "por_api_version", "asic_arg": "porrima", "fw": "1.12.1229"}, "ctc": {"fw_arg": "ctc_fw_version", "api": "CTC_NIGHTLY_1428", "api_arg": "ctc_api_version", "asic_arg": "ctc", "fw": "CTC_NIGHTLY_532"}, "ctcb": {"fw_arg": "ctcb_fw_version", "api": "CTCB_NIGHTLY_1447", "api_arg": "ctcb_api_version", "fw": "CTCB_NIGHTLY_537", "asic_arg": "ctcb"}, "lynx_400": {"fw_arg": "lynx_400_fw_version", "api": "LYNX_400_NIGHTLY_367", "api_arg": "lynx_400_api_version", "fw": "LYNX_NIGHTLY_131", "asic_arg": "lynx_400"}}
```