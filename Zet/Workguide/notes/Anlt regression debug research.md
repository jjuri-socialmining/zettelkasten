# Anlt regression debug research

Example command

```
cd regression/capella
pytest -s tests/anlt/test_anlt.py::TestAnltSingle::test_anlt_squelch -k rate_25gkr_die0_tx0_die0_rx0 --bench lynx_400_bench1
```

go to file tests/anlt/test_anlt.py

```python
def test_anlt_squelch(self, anlt_class_fixture, get_params, export_fixture, reg_parameters_fixture)
```

## Previous result check

```python
custom_params = {
    "fw_path": None,
    "bench_to_use": None,
    "build_number": 0,
    "export_to": {"type": "database", "db_table": "debug"},
    "database": {"use_db": False, "table": "debug"},
    "use_xmlrpc": False,
    "halt_of_first_error": False,
    "mcu_log_dump": False,
    "auto_ctle": 0,
    "use_pyro": [],
    "log_api_calls": [],
    "mcu_reset": True,
    "restart_mb": False,
    # Use this as an auxiliary dict for runtime values that
    # might change and are required by many fixtures
    "runtime_results": {"last_result": None},
}

get_params["runtime_results"]["last_result"]

def startup(bench, download_fw=None, mcu_reset=None, previous_result="FAILED", config_dict=None, restart_mb=False):
    def infer_args(dev):
        config_startup_dict = dict()
        config_startup_dict["hard_reset"] = restart_mb and dev in bench.dut
        # FW and dies gets complicated
        # - Download FW on the device if any of the policies match, OR
        # - there is an active die that was not active on the previous test
        device_type = "dut" if dev in bench.dut else "src"
        config_startup_dict["soft_reset"] = mcu_reset[device_type] == "always"
        policy = download_fw[device_type]
        if policy == "always" or (policy == "on_failure" and previous_result != "PASSED"):
            config_startup_dict["download_fw"] = True
            config_startup_dict["dies"] = dev.dies if config_list is None else dev.dies_from_config(config_list)
        elif policy == "once":
            if previous_result == None:
                config_startup_dict["download_fw"] = True
            else:
                config_startup_dict["download_fw"] = False
        elif policy == "never":
            config_startup_dict["download_fw"] = False
        else:
            # on_failure and previous test PASSED if there is an active die that was not used before we must download the FW again
            config_startup_dict["dies"] = dev.dies if config_list is None else dev.dies_from_config(config_list)
            config_startup_dict["download_fw"] = config_startup_dict["dies"] != dev.active_dies
        return config_startup_dict

```
`policy` is condition load fw, `once`, `always`
> Incase previous_result == None: this test case maybe the first one -> reload fw
> Incase previous_result == None: this test case maybe the first one -> reload fw

#tasks/todo/research when the previous_result is updated?