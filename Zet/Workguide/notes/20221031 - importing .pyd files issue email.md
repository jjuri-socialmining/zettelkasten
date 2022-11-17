---
title: 20221031 - importing .pyd files issue email
created: 2022-Oct-31
tags:
  - 'source'
publish: False
---


**From:** Jeff Kirsten <[jkirsten@marvell.com](mailto:jkirsten@marvell.com)>  
**Sent:** Monday, October 31, 2022 9:43 AM  
**To:** Cuong Phan <[cphan@marvell.com](mailto:cphan@marvell.com)>  
**Subject:** FW: importing .pyd files

Actually this is the latest email where I report it did work on ot-lab-7003 PC.   The problem PC is the one you and I are working on.   Those are the only two PCs I’ve tried.

But Brad finds the .pyd import works on other machines.

Jeff

**From:** Jeff Kirsten  
**Sent:** Tuesday, October 18, 2022 6:06 PM  
**To:** Brad Elliott <[belliott@marvell.com](mailto:belliott@marvell.com)>; Tim Lu <[ltim@marvell.com](mailto:ltim@marvell.com)>; Dan Nguyen <[danguyen@marvell.com](mailto:danguyen@marvell.com)>  
**Cc:** Declan McCoy <[dmccoy@marvell.com](mailto:dmccoy@marvell.com)>; Rob Bierman <[rbierman@marvell.com](mailto:rbierman@marvell.com)>; Xiao Xu <[xuxiao@marvell.com](mailto:xuxiao@marvell.com)>; Tai Ly <[ltai@marvell.com](mailto:ltai@marvell.com)>  
**Subject:** RE: importing .pyd files

Tried these tests on a second PC that is being set up in Ottawa (ot-lab7003).    This  *.pyd import problem does not appear on this second PC which is good news, but still don’t know what the difference is between the two PCs where one has the issue and one does not.

Tai’s os.path.abspath workaround described below fixes the problem but adds more complexity to the scripts as appears has to be sequenced with cache loading or load_api method as Brad suggests.   So I’d prefer to understand why the second PC works with the simple, relative path.   Will track the issue as I get more machines running and see if something new insight shakes out.

Jeff

**From:** Brad Elliott <[belliott@marvell.com](mailto:belliott@marvell.com)>  
**Sent:** Monday, October 17, 2022 7:37 AM  
**To:** Jeff Kirsten <[jkirsten@marvell.com](mailto:jkirsten@marvell.com)>; Tim Lu <[ltim@marvell.com](mailto:ltim@marvell.com)>; Dan Nguyen <[danguyen@marvell.com](mailto:danguyen@marvell.com)>  
**Cc:** Declan McCoy <[dmccoy@marvell.com](mailto:dmccoy@marvell.com)>; Rob Bierman <[rbierman@marvell.com](mailto:rbierman@marvell.com)>; Xiao Xu <[xuxiao@marvell.com](mailto:xuxiao@marvell.com)>; Tai Ly <[ltai@marvell.com](mailto:ltai@marvell.com)>  
**Subject:** RE: importing .pyd files

Are you changing directories before you import the API? I assume you’re not manually appending to the path. The append is done inside the load_api method. Typically you would load the API and then import it to register the required callbacks. Tai’s fix is fine although it will increase the length of the PATH environment variable which has limits on length. It used to be limited to 2048 characters. Maybe Windows 10 fixed that. I’ve always used relative paths to minimize the length of the environment variable.

I pushed a change to default to absolute paths when importing the API or the registers:

    [http://las-gitlab/hsc/lab/-/commit/5f0823caee0daa91ec3add842d34155411c3cf8c](http://las-gitlab/hsc/lab/-/commit/5f0823caee0daa91ec3add842d34155411c3cf8c)

Brad

**From:** Jeff Kirsten <[jkirsten@marvell.com](mailto:jkirsten@marvell.com)>  
**Sent:** Monday, October 17, 2022 12:36 AM  
**To:** Brad Elliott <[belliott@marvell.com](mailto:belliott@marvell.com)>; Tim Lu <[ltim@marvell.com](mailto:ltim@marvell.com)>; Dan Nguyen <[danguyen@marvell.com](mailto:danguyen@marvell.com)>  
**Cc:** Declan McCoy <[dmccoy@marvell.com](mailto:dmccoy@marvell.com)>; Rob Bierman <[rbierman@marvell.com](mailto:rbierman@marvell.com)>; Xiao Xu <[xuxiao@marvell.com](mailto:xuxiao@marvell.com)>; Tai Ly <[ltai@marvell.com](mailto:ltai@marvell.com)>  
**Subject:** RE: importing .pyd files

I cleared Windows PATH and PYTHONPATH of all python versions other than the one being run.   But problem still occurs.

Brad has some machines that seem to work differently than mine.  We’ll see tomorrow if we can figure out the setup differences.

Meanwhile Tai Ly came up with a fix that works using abspath when appending in the scripts:

Using this:            sys.path.append(os.path.abspath("./cache/api/por/1.12.1388"))

Instead of this:    sys.path.append("./cache/api/por/1.12.1388")

This is a good fix that I can apply.   Will just have to create the append string dynamically.   Thanks Tai.

Jeff

**From:** Brad Elliott <[belliott@marvell.com](mailto:belliott@marvell.com)>  
**Sent:** Sunday, October 16, 2022 8:06 PM  
**To:** Jeff Kirsten <[jkirsten@marvell.com](mailto:jkirsten@marvell.com)>; Tim Lu <[ltim@marvell.com](mailto:ltim@marvell.com)>; Dan Nguyen <[danguyen@marvell.com](mailto:danguyen@marvell.com)>  
**Cc:** Declan McCoy <[dmccoy@marvell.com](mailto:dmccoy@marvell.com)>; Rob Bierman <[rbierman@marvell.com](mailto:rbierman@marvell.com)>; Xiao Xu <[xuxiao@marvell.com](mailto:xuxiao@marvell.com)>; Tai Ly <[ltai@marvell.com](mailto:ltai@marvell.com)>  
**Subject:** RE: importing .pyd files

Is it possible you have a different version of python in the windows path?

**From:** Brad Elliott  
**Sent:** Sunday, October 16, 2022 11:05 PM  
**To:** Jeff Kirsten <[jkirsten@marvell.com](mailto:jkirsten@marvell.com)>; Tim Lu <[ltim@marvell.com](mailto:ltim@marvell.com)>; Dan Nguyen <[danguyen@marvell.com](mailto:danguyen@marvell.com)>  
**Cc:** Declan McCoy <[dmccoy@marvell.com](mailto:dmccoy@marvell.com)>; Rob Bierman <[rbierman@marvell.com](mailto:rbierman@marvell.com)>; Xiao Xu <[xuxiao@marvell.com](mailto:xuxiao@marvell.com)>; Tai Ly <[ltai@marvell.com](mailto:ltai@marvell.com)>  
**Subject:** RE: importing .pyd files

Can you reproduce this on multiple machines? I’ve tested the Spica5 API on three different machines and it seems to work fine (Python 3.9.13 from python.org).

Brad

**From:** Jeff Kirsten <[jkirsten@marvell.com](mailto:jkirsten@marvell.com)>  
**Sent:** Sunday, October 16, 2022 9:07 PM  
**To:** Brad Elliott <[belliott@marvell.com](mailto:belliott@marvell.com)>; Tim Lu <[ltim@marvell.com](mailto:ltim@marvell.com)>; Dan Nguyen <[danguyen@marvell.com](mailto:danguyen@marvell.com)>  
**Cc:** Declan McCoy <[dmccoy@marvell.com](mailto:dmccoy@marvell.com)>; Rob Bierman <[rbierman@marvell.com](mailto:rbierman@marvell.com)>; Xiao Xu <[xuxiao@marvell.com](mailto:xuxiao@marvell.com)>; Tai Ly <[ltai@marvell.com](mailto:ltai@marvell.com)>  
**Subject:** RE: importing .pyd files

To double-check I uninstalled Microsoft Visual C++ 2013 Redistributables for both x64 and x86, removed the msvcp120.dlls and msvcr120.dlls from both Windows directories and then reinstalled ‘Visual C++ Redistributable Packages for Visual Studio 2013’ from the link Brad sent.  But the problem persists as described in the email (only works if *_api.pyd is in same folder as launching script).

Jeff

**From:** Jeff Kirsten  
**Sent:** Saturday, October 15, 2022 11:50 AM  
**To:** Brad Elliott <[belliott@marvell.com](mailto:belliott@marvell.com)>; Tim Lu <[ltim@marvell.com](mailto:ltim@marvell.com)>; Dan Nguyen <[danguyen@marvell.com](mailto:danguyen@marvell.com)>  
**Cc:** Declan McCoy <[dmccoy@marvell.com](mailto:dmccoy@marvell.com)>; Rob Bierman <[rbierman@marvell.com](mailto:rbierman@marvell.com)>; Xiao Xu <[xuxiao@marvell.com](mailto:xuxiao@marvell.com)>; Tai Ly <[ltai@marvell.com](mailto:ltai@marvell.com)>  
**Subject:** RE: importing .pyd files

Ok.   Here is what is currently installed on that machine:

![[Pasted image 20221031100947.png]]

The link you included below resolves to:  ‘ Visual C++ Redistributable Packages for Visual Studio 2013’.   So appear that is already installed.

And in both C:\Windows\System32 and C:\Windows\SysWOW64 are already:

msvcp120.dll

msvcr120.dll

So yes Visual C++ Redistributable needs to be installed for our compiled APIs to run.  But I think this machine is already past that stage.   Note the APIs DO run if they (or more specifically the *api.pyd file) are located in the same directory as the launching script.   So as far as I can tell we are talking about something different than having  Visual C++ Redistributable installed.

Regards,

Jeff

**From:** Brad Elliott <[belliott@marvell.com](mailto:belliott@marvell.com)>  
**Sent:** Saturday, October 15, 2022 5:23 AM  
**To:** Jeff Kirsten <[jkirsten@marvell.com](mailto:jkirsten@marvell.com)>; Tim Lu <[ltim@marvell.com](mailto:ltim@marvell.com)>; Dan Nguyen <[danguyen@marvell.com](mailto:danguyen@marvell.com)>  
**Cc:** Declan McCoy <[dmccoy@marvell.com](mailto:dmccoy@marvell.com)>; Rob Bierman <[rbierman@marvell.com](mailto:rbierman@marvell.com)>; Xiao Xu <[xuxiao@marvell.com](mailto:xuxiao@marvell.com)>; Tai Ly <[ltai@marvell.com](mailto:ltai@marvell.com)>  
**Subject:** RE: importing .pyd files

This does not have to do with the API. There is something wrong with the machine you are using. The most likely problem is that the Visual Studio Runtime libraries are not installed correctly. The API build machine is setup to compile with Visual Studio Express 2013. If you’re going to use a 64b python you need the 64b binaries installed:

    [https://www.microsoft.com/en-ca/download/details.aspx?id=40784](https://www.microsoft.com/en-ca/download/details.aspx?id=40784)

There are two files that are required from this package:

    msvcp120.dll

    msvcr120.dll

The 64b versions will reside in the C:/Windows/System32 directory. The 32b versions will reside in the C:/Windows/SysWOW64 folder. If you search the System32 directory and don’t find these files then you need to setup the above package. If you’ve copied them manually for testing you need to make sure you’ve deleted them.

Brad

**From:** Jeff Kirsten <[jkirsten@marvell.com](mailto:jkirsten@marvell.com)>  
**Sent:** Saturday, October 15, 2022 1:20 AM  
**To:** Tim Lu <[ltim@marvell.com](mailto:ltim@marvell.com)>; Brad Elliott <[belliott@marvell.com](mailto:belliott@marvell.com)>; Dan Nguyen <[danguyen@marvell.com](mailto:danguyen@marvell.com)>  
**Cc:** Declan McCoy <[dmccoy@marvell.com](mailto:dmccoy@marvell.com)>; Rob Bierman <[rbierman@marvell.com](mailto:rbierman@marvell.com)>; Xiao Xu <[xuxiao@marvell.com](mailto:xuxiao@marvell.com)>; Tai Ly <[ltai@marvell.com](mailto:ltai@marvell.com)>  
**Subject:** RE: importing .pyd files

The problem boils down to a simple test that can be demonstrated with both PG2 and Spica5 APIs using either Python 3.9 32-bit or Python 3.9 64-bit from python.org.   We can leave Anaconda out of this.   And occurs running PyCharm or running Python from command line, so PyCharm isn’t a factor either.

The test uses only the *_api.py and *_api.pyd files and a launch script with a single import statement:

-   As long as the *_api.pyd file is in the SAME folder as the launch script (Python current directory) the import statement imports *_api.py which in turns imports *_api.pyd.
-   If the *_api.pyd is in a DIFFERENT folder than the launch script the *_api.pyd will not import regardless of setting path to point to that different folder.  (You can put *_api.py in that different folder but *_api.pyd in same folder as launch script and everything will import.)

So this problem manifests therefore when using Brad’s method of downloading APIs to a cache folder which is different from the folder the test launch script resides in.  This is a reasonable case and seems could arise in most anyone’s software setup.   But if SW team does a simple import test with everything in same folder the problem won’t appear.

I’ve searched the web and seen some references to .pyd files importing differently than .py files but no good solutions.

Who can help on this?

Regards,

Jeff

**From:** Tim Lu <[ltim@marvell.com](mailto:ltim@marvell.com)>  
**Sent:** Friday, October 14, 2022 9:12 AM  
**To:** Brad Elliott <[belliott@marvell.com](mailto:belliott@marvell.com)>; Jeff Kirsten <[jkirsten@marvell.com](mailto:jkirsten@marvell.com)>; Dan Nguyen <[danguyen@marvell.com](mailto:danguyen@marvell.com)>  
**Cc:** Declan McCoy <[dmccoy@marvell.com](mailto:dmccoy@marvell.com)>; Rob Bierman <[rbierman@marvell.com](mailto:rbierman@marvell.com)>; Xiao Xu <[xuxiao@marvell.com](mailto:xuxiao@marvell.com)>  
**Subject:** RE: importing .pyd files

+ Xiao

In that case, I would recommend us to download whatever version is recommended through python.org.  What we could do is to create a python flow document to show steps to install python 3.x and with Spyder, PyScripter, and PyCharm IDE.  Is there a similar version FW have for new hire?

Jeff and Xiao, perhaps something you two can help?  Xiao, I know you tested python 3.x standalone w/ Spyder…  I know pyscripter is easy to do.  Who can take on Pycharm?

Regards,

Tim Lu

**From:** Brad Elliott <[belliott@marvell.com](mailto:belliott@marvell.com)>  
**Sent:** Friday, October 14, 2022 9:03 AM  
**To:** Tim Lu <[ltim@marvell.com](mailto:ltim@marvell.com)>; Jeff Kirsten <[jkirsten@marvell.com](mailto:jkirsten@marvell.com)>; Dan Nguyen <[danguyen@marvell.com](mailto:danguyen@marvell.com)>  
**Cc:** Declan McCoy <[dmccoy@marvell.com](mailto:dmccoy@marvell.com)>; Rob Bierman <[rbierman@marvell.com](mailto:rbierman@marvell.com)>  
**Subject:** RE: importing .pyd files

I don’t have any issue using the Spica5 API on 64b python 3.9 (python.org/downloads) from the lab directory on multiple lab machines. The was an issue with the 64b API build a few weeks ago but that problem appears to have been resolved.

We’re not allowed to use Anaconda anymore as it requires a commercial license (unless Marvell has one). I don’t know what the SSL error is. I assume that’s a problem with Anaconda. I would guess there is an environment variable set that is pointing to the wrong version of Python.

Brad

**From:** Tim Lu <[ltim@marvell.com](mailto:ltim@marvell.com)>  
**Sent:** Friday, October 14, 2022 11:42 AM  
**To:** Jeff Kirsten <[jkirsten@marvell.com](mailto:jkirsten@marvell.com)>; Brad Elliott <[belliott@marvell.com](mailto:belliott@marvell.com)>; Dan Nguyen <[danguyen@marvell.com](mailto:danguyen@marvell.com)>  
**Cc:** Declan McCoy <[dmccoy@marvell.com](mailto:dmccoy@marvell.com)>; Rob Bierman <[rbierman@marvell.com](mailto:rbierman@marvell.com)>  
**Subject:** RE: importing .pyd files

Hi Jeff K,

Sorry late to this topic.  Question:

1.       Have we tried native Python 3.9 version installed

2.       Use simple IDE to do the same testing your have done and does it have the same issue?

a.       Basically, I want to know if this is an Anaconda, Python 3.9, or ODSP flow issue

Regards,

Tim Lu

**From:** Jeff Kirsten <[jkirsten@marvell.com](mailto:jkirsten@marvell.com)>  
**Sent:** Thursday, October 13, 2022 6:01 PM  
**To:** Brad Elliott <[belliott@marvell.com](mailto:belliott@marvell.com)>; Dan Nguyen <[danguyen@marvell.com](mailto:danguyen@marvell.com)>  
**Cc:** Declan McCoy <[dmccoy@marvell.com](mailto:dmccoy@marvell.com)>; Rob Bierman <[rbierman@marvell.com](mailto:rbierman@marvell.com)>  
**Subject:** RE: importing .pyd files

I have been running the straight Python 3.9 64-bit distribution so far.  Read on a website somewhere that Anaconda distribution handles .pyd imports better (no idea why that would be the case).   

So I tried running with Python 3.9 64-bit Anaconda .   Results were:

·         The ‘_por_api.pyd’ import from por_api.py problem got fixed!  Runs with the already existing cache.

·         However if the cache is removed it won’t rebuild.  Failure when trying to load cache is: 

![[Pasted image 20221031100912.png]]

This is similar to the first error we were trying to fix:  a .pyd won’t import from .py file.  In this case the .pyd is in a different directory than the .py, but is all part of the Anaconda distribution so seems it ought to be able to work itself out.

Stumped again.

Jeff

**From:** Jeff Kirsten  
**Sent:** Thursday, October 13, 2022 6:37 AM  
**To:** Brad Elliott <[belliott@marvell.com](mailto:belliott@marvell.com)>; Dan Nguyen <[danguyen@marvell.com](mailto:danguyen@marvell.com)>  
**Cc:** Declan McCoy <[dmccoy@marvell.com](mailto:dmccoy@marvell.com)>; Rob Bierman <[rbierman@marvell.com](mailto:rbierman@marvell.com)>  
**Subject:** RE: importing .pyd files

Ok.  Any ideas how to get this _por_api.pyd import to work more deterministically?   I don’t see anything that is incorrect in how my environment is running it.   If this type of import works in some cases but not in mine seems something is not nailed down correctly.

I can try some more things but would be surprised somehow if I’m the first one seeing this issue.

Regards,

Jeff

**From:** Brad Elliott <[belliott@marvell.com](mailto:belliott@marvell.com)>  
**Sent:** Thursday, October 13, 2022 4:24 AM  
**To:** Jeff Kirsten <[jkirsten@marvell.com](mailto:jkirsten@marvell.com)>; Dan Nguyen <[danguyen@marvell.com](mailto:danguyen@marvell.com)>  
**Cc:** Declan McCoy <[dmccoy@marvell.com](mailto:dmccoy@marvell.com)>; Rob Bierman <[rbierman@marvell.com](mailto:rbierman@marvell.com)>  
**Subject:** RE: importing .pyd files

You can’t avoid the .pyd. It’s the actual API wrapped in a DLL. The .py is just a wrapper that tells python how to call functions in the DLL/PYD.

Compiling the API on the target machine is possible but it requires a compiler installed on every machine which is a non-trivial exercise. We’re currently using Visual Studio to build the API but we can’t use that on lab machines since it requires a license. I was working on switching to MingW64 as a build environment but I haven’t deployed that. I was trying to get MSYS2 to work but newer versions don’t support Olympus.pyd.

Brad

**From:** Jeff Kirsten <[jkirsten@marvell.com](mailto:jkirsten@marvell.com)>  
**Sent:** Wednesday, October 12, 2022 6:46 PM  
**To:** Brad Elliott <[belliott@marvell.com](mailto:belliott@marvell.com)>; Dan Nguyen <[danguyen@marvell.com](mailto:danguyen@marvell.com)>  
**Cc:** Declan McCoy <[dmccoy@marvell.com](mailto:dmccoy@marvell.com)>; Rob Bierman <[rbierman@marvell.com](mailto:rbierman@marvell.com)>  
**Subject:** RE: importing .pyd files

Specifically the problem is as follows:

·         Application program runs in directory ‘api_target_connector’

·         ‘cache’ gets generated in directory ‘1.12.1388’

![[Pasted image 20221031100849.png]]

·         In ‘1.12.1388’ are files ‘por_api.py’ and ‘_por_api.pyd’.    

·         Launch program in directory ‘api_target_connector’ tries to import ‘por_api.py’.  

·         Inside ‘por_api.py’ are the lines:

![[Pasted image 20221031100834.png]]

·         Last line therefore tries to import  ‘_por_api.pyd’ but fails with message:  ImportError: DLL load failed while importing _por_api: The parameter is incorrect.

Experimentation shows:

·         If put ‘_por_api.pyd’ in same folder as launch program (directory ‘api_target_connector’) then import works.

·         Can modify ‘por_api.py’ to make it import a .py file from same directory ‘1.12.1388’.   While importing a .pyd from same directory does not work.

Simple conclusion:

There seems to be more trouble getting *.pyd files to import In a chain of imports that getting .py files to import.   Do we really need .pyd file(s) in our API build distributions?

Jeff

**From:** Jeff Kirsten  
**Sent:** Wednesday, October 12, 2022 1:55 PM  
**To:** Brad Elliott <[belliott@marvell.com](mailto:belliott@marvell.com)>  
**Cc:** Declan McCoy <[dmccoy@marvell.com](mailto:dmccoy@marvell.com)>; Rob Bierman <[rbierman@marvell.com](mailto:rbierman@marvell.com)>  
**Subject:** importing .pyd files

Hi Brad,

I’ve done quite a bit more work on PG2 with Python 3.9 since we last spoke.   I am seeing cases where import of _por_api.pyd file is failing in one set of scripts but works in another set of scripts.

This bring up a general question:  Are we causing unnecessary complication by distributing api builds with *.pyd files?    If we just shipped out only *.py files and let the .pyd be generated when first run would we avoid difficulty of having to match Python versions, 32/64-bit environments, etc.?     Even when I believe I’m doing everything right in the environment and importing from the right place problems seem to come up that haven’t been easy to figure out.

Similarly when Declan finds Spica5 api works with 32-bit but not 64-bit would that be avoided if no .pyd files?

Regards,

Jeff

