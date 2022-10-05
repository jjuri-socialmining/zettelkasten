---
title: strip feature error
created: 2022-Jun-08
tags:
  - 'permanent/fact'
---




```
Failed parsing feature at src/generic/hsc_dev_private.h:L108
Traceback (most recent call last):
  File "/cygdrive/c/Users/dutran/projects/hsc/lynx/api//../../../bin/strip_features.py", line 976, in <module>
    parser.strip_features(name, features_to_keep, options.test, comment_format=comment_format, output_path=options.output)
  File "/cygdrive/c/Users/dutran/projects/hsc/lynx/api//../../../bin/strip_features.py", line 704, in strip_features
    (output, last_pos) = self._strip_features(contents, features, features_to_keep, last_pos, path)
  File "/cygdrive/c/Users/dutran/projects/hsc/lynx/api//../../../bin/strip_features.py", line 379, in _strip_features
    feat_end_begin = features[feature]["feat_end_begin"]
KeyError: 'feat_end_begin'
make: *** [project/amalgamated.inc:38: build-output/events/stripped] Error 1
```
