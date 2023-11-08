# CHANGELOG



## v0.10.0 (2023-11-08)

### Feature

* feat: add breaking change detection to CICD ([`2177f6c`](https://github.com/ELC/pycracks/commit/2177f6cae696b83d7fdef6d5d53425aadba80b79))

### Fix

* fix: use typing for built in tuple ([`8fd17ea`](https://github.com/ELC/pycracks/commit/8fd17ea78c2419aaac5b96f95706af499c56982c))

* fix(compatibility): use typing_extensions to support Python 3.8 ([`f78080a`](https://github.com/ELC/pycracks/commit/f78080af550d0baab2bf7915dd1b967f30c36c67))

* fix: use local version to check breaking changes ([`56323fc`](https://github.com/ELC/pycracks/commit/56323fc965b0c75ecfbb8bdc23f8562ca28a12e6))


## v0.9.0 (2023-11-07)

### Feature

* feat: add pre-commit check to CICD ([`3c38ac6`](https://github.com/ELC/pycracks/commit/3c38ac687b20c89da6c1ee2da7399c5459655a70))

### Unknown

* Merge branch &#39;master&#39; of https://github.com/ELC/pycracks ([`bdc8c55`](https://github.com/ELC/pycracks/commit/bdc8c55071b2cf727a2d5c243585d3915524418d))


## v0.8.0 (2023-11-07)

### Feature

* feat: add pre-commit hooks ([`0e47f25`](https://github.com/ELC/pycracks/commit/0e47f25997c01c4b81b60e24d8aa3b267ae57578))


## v0.7.0 (2023-11-07)

### Feature

* feat: add testing to CICD ([`e27773e`](https://github.com/ELC/pycracks/commit/e27773edb8d9bad1ee23cd07c804d9c42153071f))

### Fix

* fix(test): make hypothesis less strict ([`23899c1`](https://github.com/ELC/pycracks/commit/23899c16c2d9cabf89d57156794415294ba6feff))

* fix(cicd): remove required python version in pipfile ([`c324399`](https://github.com/ELC/pycracks/commit/c324399f405decc0d2029dee75bed50359ef8217))

* fix(test): make python version 3.8+ ([`3c9e1fa`](https://github.com/ELC/pycracks/commit/3c9e1fa14265bcbcf26e8b5f5aa87f4d081225af))

### Unknown

* Merge branch &#39;master&#39; of https://github.com/ELC/pycracks ([`b0035bb`](https://github.com/ELC/pycracks/commit/b0035bbbda2679de13221ab87b0f8ba2a780f2a4))

* Merge branch &#39;master&#39; of https://github.com/ELC/pycracks ([`42adb0d`](https://github.com/ELC/pycracks/commit/42adb0db76197000faf0ef4667533ac9c1a8f479))


## v0.6.0 (2023-11-07)

### Feature

* feat: add unit test with partial coverage ([`670f5da`](https://github.com/ELC/pycracks/commit/670f5dadea5586cb34119ebf559b3274bbfbe624))


## v0.5.7 (2023-11-04)

### Fix

* fix: use file to store changelog body ([`e089ed6`](https://github.com/ELC/pycracks/commit/e089ed6bc6afa0a3836f9882140a0fa87b7b1821))


## v0.5.6 (2023-11-04)

### Fix

* fix: use raw string from changelog ([`e9c2ecb`](https://github.com/ELC/pycracks/commit/e9c2ecb55c481d0e97055e48bd325c092263889c))


## v0.5.5 (2023-11-04)

### Fix

* fix(release): install changelog-parser globally ([`67ccefe`](https://github.com/ELC/pycracks/commit/67ccefe6afb728cc94b21b96e7593815d4c4783d))


## v0.5.4 (2023-11-04)

### Fix

* fix(changelog-parser): use results as is from jq ([`a5b5c8b`](https://github.com/ELC/pycracks/commit/a5b5c8b4c636595b73a0509eae2d55752b775df8))


## v0.5.3 (2023-11-04)

### Fix

* fix(release): remove explicit node version ([`1214f1d`](https://github.com/ELC/pycracks/commit/1214f1d19cb060369c6d3a2ba19db9d66c214d18))


## v0.5.2 (2023-11-04)

### Fix

* fix(release): change changelog parser ([`1243e15`](https://github.com/ELC/pycracks/commit/1243e151dd1e30cd3aa4d6d83a8a822b5b64fff0))


## v0.5.1 (2023-11-04)

### Fix

* fix(release): remove explicit version ([`cfab52e`](https://github.com/ELC/pycracks/commit/cfab52ea48fdb26900b9c94c03d52e9f570c47e1))


## v0.5.0 (2023-11-04)

### Feature

* feat(release): add body to Github release from Changelog ([`ba89a16`](https://github.com/ELC/pycracks/commit/ba89a16d88183f321a1b4065fdb419a8f810750d))


## v0.4.1 (2023-11-04)

### Fix

* fix(cicd): remove wrong characters ([`b9958a5`](https://github.com/ELC/pycracks/commit/b9958a526b7244af43a06012b841b2a48b3a908b))


## v0.4.0 (2023-11-04)

### Feature

* feat(cicd): add Github Release step ([`8265f69`](https://github.com/ELC/pycracks/commit/8265f694634156ee935a73a844e18687daada39e))


## v0.3.0 (2023-11-04)

### Feature

* feat: abort if same version as target ([`fdcc7d3`](https://github.com/ELC/pycracks/commit/fdcc7d3b70145046f0fee84743d26b319a2d3a08))


## v0.2.1 (2023-11-03)

### Fix

* fix(release): update tagging ([`02e1c82`](https://github.com/ELC/pycracks/commit/02e1c82e1d02b804d31ef6e6ce13c8cd0332959f))


## v0.2.0 (2023-11-03)

### Feature

* feat: test semantic releases ([`ea37095`](https://github.com/ELC/pycracks/commit/ea37095679796ec7fbcc213c4da6988a101a01dc))

* feat: release minimum viable product ([`d638669`](https://github.com/ELC/pycracks/commit/d638669255da7c30c5bc35085f67f5598dfade11))
