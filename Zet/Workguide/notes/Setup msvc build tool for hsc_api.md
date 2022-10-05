---
title: Setup msvc build tool for hsc_api
created: 2022-Feb-15
tags:
  - 'permanent/howto'
---

To import hsc_api file, we need to setup environment with msvs that work with python version or we will face the error.

```
    import _hsc_api
ImportError: DLL load failed while importing _hsc_api: The parameter is incorrect.
```

Some background and explanations:

1.  Python3.9 was released in mid of 2019. For Windows, it was probably developed with C/C++ 2017 tools. As you know, Python is actually developed and built in C/C++ and many of the “optimized” libraries (such as numpy) are C libraries, Python simply provides the interface.
2.  Python3.10 was released in late 2021. The Windows version was developed with Windows C/C++ 2019 tools.
3.  We were able to import and make use of the Python3.10 APIs in some PCs, but not on others. The PCs where the API worked come with Microsoft Visual C/C++ (MSVC) 2019 Redistributable installed. The PCs where the API did not work were older and did not have MSVC 2019 installed.
4.  The Python3.10 APIs had MSVC 2019 specific dependencies. Therefore when attempting to import the .pyd we got “DLL Load failed: The specified module could not be found”. Python could find the pyd, but not some of the pyd dependencies.

The solution:

1.  Install MSVC redistributable 2015-2022 (x86 and 64-bit), which contains the required 2019 version: [https://docs.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist?view=msvc-170](https://docs.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist?view=msvc-170).
2.  Install Visual Studio 2019: [https://docs.microsoft.com/en-us/visualstudio/releases/2019/release-notes](https://docs.microsoft.com/en-us/visualstudio/releases/2019/release-notes)
3.  In the Visual Studio installer options:

1.  Mark the “Desktop development with C++” option (marking it will include all the essential tools) under “Desktop & Mobile”.
2.  Mark “Python native development tools” option under Web & Cloud -> Python development.

After applying these steps I was able to run a regression in SJCLab-007265 CTCA<>Lynx400 setup, meaning I was finally able to successfully test CTC, CTCB, Lynx400 API.