# elfstats-env

A Python virtual environment which is used in `elfstats` project to support [elfstatsd][] and [elfstats-munin][].

This repository contains source files to build RPM package with a virtual environment for Red Hat Enterprise Linux 6 (RHEL6). This virtual environment will be installed into `/srv/virtualenvs/elfstats`. The environment contains all Python packages needed for `elfstats` to operate.

## Requirements

* Red Hat Enterprise Linux 6 with Python 2.6.x installed

## Build

* `git clone https://github.com/dzzh/elfstats-env.git` 
* `cd elfstats-env`
* `rpmbuild -bb SPECS/elfstats-env.spec`

The resulting RPM will be placed in `RPMS/$YOUR_PLATFORM` directory.

## Installation

Build an RPM following the procedure described in Build section and run `sudo yum install elfstats-env-X.X.X-X.el6.xXX.rpm`. 

## elfstats on other operating systems

If you work with different operating system but still want to benefit from `elfstats` project, you can either install it using your default Python or create a virtual environment yourself. You can find more information about this procedure in [readme](https://github.com/dzzh/elfstatsd/blob/master/README.md) for `elfstatsd`.

## License

Eelfstatsd is available under the terms of MIT License.

Copyright © 2013 [Źmicier Žaleźničenka][me] & Andriy Yakovlev.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

[me]: https://github.com/dzzh
[elfstatsd]: https://github.com/dzzh/elfstatsd
[elfstats-munin]: https://github.com/dzzh/elfstats-munin