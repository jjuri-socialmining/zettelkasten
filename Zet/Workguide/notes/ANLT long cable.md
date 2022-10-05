up:: [[ANLT MOC]]
# ANLT long cable

- Reduce target SNR
```python
p_anlt_rules.lt.target_snr = 18000
```
- Enable FIR walk
```python
p_anlt_rules.lt.bypass_fir_walk = False
```
- Set CTLE Tune
```python
p_anlt_rules.lt.ctle_tune = True
```
```python
#tx.fir_tap    = [[0, 0, 0, 0, -150, 550, -220],[0, 0, 0, 0, -150, 550, -220],[0, 0, 0, 0, -150, 550, -220],[0, 0, 0, 0, -150, 550, -220],[0, 0, 0, 0, -150, 550, -220],[0, 0, 0, 0, -150, 550, -220],[0, 0, 0, 0, -150, 550, -220],[0, 0, 0, 0, -150, 550, -220]]
rx.dsp_mode     = CPL_DSP_MODE_DFE1_RC_DFE2
rx.ctle_code    = [31] * 8
rx.afe_trim     = [CPL_AFE_TRIM_NEG_4dB] * 8
```

