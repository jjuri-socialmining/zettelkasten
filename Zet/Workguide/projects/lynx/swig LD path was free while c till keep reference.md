---
title: swig LD path was free while c till keep reference
created: 2022-Sep-21
tags:
  - 'issue/done'
project: TBD
date:
  - start: 2022-09-21
  - end: 'TBD'
  - due: 'TBD'
---
up:: [[Issues list]], [[Tiny logger|tlog]]

![[20220921143210 ~ swig ld path.png]]

set ld path
http://las-gitlab/hsc/capi/-/merge_requests/205

```c++
hsc_status_t wrap_hsc_mcu_log_ld_file_set(PyObject *pyself, PyObject *ld_path)

{
	int res = 0;
	void *c_self = 0;
	hsc_mcu_t *c_mcu = 0;
	char *char_content = NULL;

	/* Get C object */
	res = SWIG_ConvertPtr(pyself, &c_self,SWIGTYPE_p_hsc_mcu_s, 0);
	if (!SWIG_IsOK(res))
	{
		SWIG_exception_fail(SWIG_ArgError(res), "in method '" "hsc_mcu_log_ld_set" "', argument " "1"" of type '" "hsc_mcu_t *""'");
	}
	c_mcu = reinterpret_cast< hsc_mcu_t * >(c_self);
	char_content = SWIG_Python_str_AsChar(ld_path);
	return (hsc_status_t)hsc_mcu_log_ld_file_set(c_mcu,(const char *)char_content);
fail:
	return INPHI_ERROR;
}
```

Mr [[Nam Nguyễn]] Solution:
![[20220922092014 ~ Tlog ld path.png]]