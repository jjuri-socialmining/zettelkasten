---
title: '@ learn.microsoft.com, Exporting from a DLL Using DEF Files'
UID: 221028224137
tags:
  - 'created/2022/Oct/28'
  - 'source/article'
publish: False
---
- metadata:
	- url:: https://learn.microsoft.com/en-us/cpp/build/exporting-from-a-dll-using-def-files?view=msvc-170
	- author::
	- category::

### In this article

1.  [What do you want to do?](chrome-extension://pcmpcfapbekmbjjkdalcgopdkipoggdi/_generated_background_page.html#what-do-you-want-to-do)
2.  [What do you want to know more about?](chrome-extension://pcmpcfapbekmbjjkdalcgopdkipoggdi/_generated_background_page.html#what-do-you-want-to-know-more-about)
3.  [See also](chrome-extension://pcmpcfapbekmbjjkdalcgopdkipoggdi/_generated_background_page.html#see-also)

A module-definition or DEF file (\*.def) is a text file containing one or more module statements that describe various attributes of a DLL. If you are not using the **`__declspec(dllexport)`** keyword to export the DLL's functions, the DLL requires a DEF file.

A minimal DEF file must contain the following module-definition statements:

-   The first statement in the file must be the LIBRARY statement. This statement identifies the DEF file as belonging to a DLL. The LIBRARY statement is followed by the name of the DLL. The linker places this name in the DLL's import library.
    
-   The EXPORTS statement lists the names and, optionally, the ordinal values of the functions exported by the DLL. You assign the function an ordinal value by following the function's name with an at sign (@) and a number. When you specify ordinal values, they must be in the range 1 through N, where N is the number of functions exported by the DLL. If you want to export functions by ordinal, see [Exporting Functions from a DLL by Ordinal Rather Than by Name](https://learn.microsoft.com/en-us/cpp/build/exporting-functions-from-a-dll-by-ordinal-rather-than-by-name?view=msvc-170) as well as this topic.
    

For example, a DLL that contains the code to implement a binary search tree might look like the following:

```
LIBRARY   BTREE
EXPORTS
   Insert   @1
   Delete   @2
   Member   @3
   Min   @4
```

If you use the [MFC DLL Wizard](https://learn.microsoft.com/en-us/cpp/mfc/reference/mfc-dll-wizard?view=msvc-170) to create an MFC DLL, the wizard creates a skeleton DEF file for you and automatically adds it to your project. Add the names of the functions to be exported to this file. For non-MFC DLLs, create the DEF file yourself and add it to your project. Then go to **Project** > **Properties** > **Linker** > **Input** > **Module Definition File** and enter the name of the DEF file. Repeat this step for each configuration and platform, or do it all at once by selecting **Configuration = All Configurations**, and **Platform = All Platforms**.

If you are exporting functions in a C++ file, you have to either place the decorated names in the DEF file or define your exported functions with standard C linkage by using extern "C". If you need to place the decorated names in the DEF file, you can obtain them by using the [DUMPBIN](https://learn.microsoft.com/en-us/cpp/build/reference/dumpbin-reference?view=msvc-170) tool or by using the linker [/MAP](https://learn.microsoft.com/en-us/cpp/build/reference/map-generate-mapfile?view=msvc-170) option. Note that the decorated names produced by the compiler are compiler specific. If you place the decorated names produced by the Microsoft C++ compiler (MSVC) into a DEF file, applications that link to your DLL must also be built using the same version of MSVC so that the decorated names in the calling application match the exported names in the DLL's DEF file.

Note

A DLL built with Visual Studio 2015 can be consumed by applications built with Visual Studio 2017 or Visual Studio 2019.

If you are building an [extension DLL](https://learn.microsoft.com/en-us/cpp/build/extension-dlls-overview?view=msvc-170), and exporting using a DEF file, place the following code at the beginning and end of your header files that contain the exported classes:

```
#undef AFX_DATA
#define AFX_DATA AFX_EXT_DATA
// <body of your header file>
#undef AFX_DATA
#define AFX_DATA
```

These lines ensure that MFC variables that are used internally or that are added to your classes are exported (or imported) from your MFC extension DLL. For example, when deriving a class using `DECLARE_DYNAMIC`, the macro expands to add a `CRuntimeClass` member variable to your class. Leaving out these four lines might cause your DLL to compile or link incorrectly or cause an error when the client application links to the DLL.

When building the DLL, the linker uses the DEF file to create an export (.exp) file and an import library (.lib) file. The linker then uses the export file to build the DLL file. Executables that implicitly link to the DLL link to the import library when they are built.

Note that MFC itself uses DEF files to export functions and classes from the MFCx0.dll.
