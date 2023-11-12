# CHANGELOG



## v0.14.3 (2023-11-12)

### Fix

* fix: add trove classifiers ([`bba2a95`](https://github.com/ELC/pycracks/commit/bba2a95c27038512b35a22028113ac49c7246d69))


## v0.14.2 (2023-11-12)

### Fix

* fix: update license in PyPI ([`0c87808`](https://github.com/ELC/pycracks/commit/0c87808165ad05c58efd9819d938e69dd0477ad1))


## v0.14.1 (2023-11-12)

### Fix

* fix: combine permission levels ([`e05bd5d`](https://github.com/ELC/pycracks/commit/e05bd5d72005d0c6389826738ae8604792aa1115))


## v0.14.0 (2023-11-12)

### Feature

* feat(cicd): combine check and test pipelines ([`a28cf2e`](https://github.com/ELC/pycracks/commit/a28cf2e43970811409972c22983dc5b556919b85))

### Fix

* fix(cicd): use global pipenv as default test command ([`f0d26cc`](https://github.com/ELC/pycracks/commit/f0d26cc6ae94172b03283f56f23c4e9a664b8e6a))

* fix(cicd): attach head ([`bc52c89`](https://github.com/ELC/pycracks/commit/bc52c89c601c0aa6222719f90b90786dc5edfcc3))

* fix(cicd): check breaking changes in matrix ([`c0e13b8`](https://github.com/ELC/pycracks/commit/c0e13b8761aef174f8e1bdc5086999c9ed036400))

* fix(cicd): run tests after checks ([`b90249d`](https://github.com/ELC/pycracks/commit/b90249d9f617a4cf0f7efe5584200585801abb46))

* fix(cicd): tag without a message ([`380361c`](https://github.com/ELC/pycracks/commit/380361c8e188e7dec381d67ee5e765e9fe6902d2))


## v0.13.0 (2023-11-12)

### Feature

* feat(cicd): use tursted publisher for PyPI ([`ce434b1`](https://github.com/ELC/pycracks/commit/ce434b1c421c4c8b52f3e4ad1623fc1bcee1c8d3))

* feat(cicd): divide pipelines into composable parts ([`2bd2a82`](https://github.com/ELC/pycracks/commit/2bd2a82b12a0c8c541b9ae070cf7e3b5217e0689))

### Fix

* fix(cicd): update job condition ([`acb960c`](https://github.com/ELC/pycracks/commit/acb960ca4f36e2a9713fe1c5b17dd598c412c317))

* fix(cicd): run tests on all branches ([`df77bc6`](https://github.com/ELC/pycracks/commit/df77bc6b04b2717af9f52fc3ca583866ab398ade))

* fix(cicd): add permission to generate token ([`67ea2d6`](https://github.com/ELC/pycracks/commit/67ea2d6ee44ffec089ba9b5e9903f7ff0e2a4b47))

* fix(cicd): tag last commit that is not a merge ([`3decf27`](https://github.com/ELC/pycracks/commit/3decf2779c4ea3fcf5a984e30d4c5ae6ee83f7a1))

* fix(cicd): remove redudant trigger ([`00e3667`](https://github.com/ELC/pycracks/commit/00e3667b2212d5ad38851513381e3d4b9f8733e9))

* fix(cicd): fix branch triggers ([`0a7ff99`](https://github.com/ELC/pycracks/commit/0a7ff992fe435c6b1dce8d84e820e28e6f8d893f))

* fix: update license information for PyPI ([`e356913`](https://github.com/ELC/pycracks/commit/e3569138ca3b910e7773b68ad8724e81f37c6d31))


## v0.12.1 (2023-11-12)

### Fix

* fix(cicd): deploy only after test status is updated ([`25a079b`](https://github.com/ELC/pycracks/commit/25a079b6c067aa6b6e9f62b431bb11c45b10cf4d))


## v0.12.0 (2023-11-12)

### Fix

* fix(cicd): remove custom action for test reports ([`b82e79b`](https://github.com/ELC/pycracks/commit/b82e79b9912a292d8c1fcef2853c096808601a24))

* fix(cicd): make format explicit ([`af45e2a`](https://github.com/ELC/pycracks/commit/af45e2ab2b08dcb72e5aafa1c674914dc64ba2da))

* fix(cicd): use same report for coveralls ([`96adb89`](https://github.com/ELC/pycracks/commit/96adb89fd0b9676299ac72081141aa74b09b99a6))

* fix(cicd): add title to distinguish between versions ([`db8aac5`](https://github.com/ELC/pycracks/commit/db8aac5970e63f28d38211cfa10a8a5789ca72fe))

* fix(cicd): update comments with matrix support ([`1d34aa7`](https://github.com/ELC/pycracks/commit/1d34aa79d5c95aa42ab052e8cb1d066b1d07543e))

* fix(cicd): always run report upload ([`b703733`](https://github.com/ELC/pycracks/commit/b7037331691f8eb244fcc687b198d0354f408063))

* fix(cicd): update test report for pytest ([`ad5e9f2`](https://github.com/ELC/pycracks/commit/ad5e9f20131484288c32ea3a55622ff1ef4e3f33))

* fix(release): remove debug mode ([`cacf28b`](https://github.com/ELC/pycracks/commit/cacf28b5e0f5ef864a0f3616292dd8680c0bd667))

* fix(release): use debug mode in coveralls ([`cbc94bd`](https://github.com/ELC/pycracks/commit/cbc94bdbafc6f78e77006cf586d768fdfc4aeb61))

* fix(cicd): finish explicit flags ([`c956afe`](https://github.com/ELC/pycracks/commit/c956afec7507df8c8416f2de82327fd117a55185))

* fix(release): ignore merge commits ([`c4d5a2f`](https://github.com/ELC/pycracks/commit/c4d5a2f430baec4a4e0efae8e7fd313bce5bce0d))


## v0.11.0 (2023-11-12)

### Feature

* feat(cicd): use hosted pre-commit.ci ([`d2ba540`](https://github.com/ELC/pycracks/commit/d2ba5402cb86a07f308425fc48dd89ab03e1e028))

* feat(cicd): use hosted pre-commit.ci ([`c7fe60b`](https://github.com/ELC/pycracks/commit/c7fe60bdf61e1eff4710d666a87a61f74720c4db))

* feat(cicd): add test report ([`2c77430`](https://github.com/ELC/pycracks/commit/2c77430f4db3c02fd212fa1191254825b3b2e159))

### Fix

* fix(cicd): add test-finish step ([`e1082f1`](https://github.com/ELC/pycracks/commit/e1082f119a93e60e224cf122d6ce464130f8eab7))

* fix(cicd): remove manual file specification in coveralls ([`cf808bb`](https://github.com/ELC/pycracks/commit/cf808bb6490fd40bf6cffab4d892e09cb0783be9))

* fix: use official coveralls action ([`92ae4d6`](https://github.com/ELC/pycracks/commit/92ae4d6a5f1cac11ff385a2a447016cf9da4c4b6))

* fix(cicd): test alternative test reporter ([`d18bae1`](https://github.com/ELC/pycracks/commit/d18bae10ade842a9df85cbe60b3224b671e5b911))

* fix(cid): modify permisisons ([`7c4ab2d`](https://github.com/ELC/pycracks/commit/7c4ab2d31f555c28022d14340d677cc96eb360be))

* fix(cicd): only run deploy on master ([`94cef80`](https://github.com/ELC/pycracks/commit/94cef80f145d42e6f0e94750a6970c47bffab922))

* fix(cicd): use test reporter with JUnit ([`716371b`](https://github.com/ELC/pycracks/commit/716371bfb038650d2107c093a22baf6afa89b416))

* fix(cicd): cancell previous run on new commits ([`809ecf0`](https://github.com/ELC/pycracks/commit/809ecf0c6729ab8b0a89bdd0854e45a4b760aca8))

* fix(cicd): use global write permissions for pull-requests ([`d5c0f55`](https://github.com/ELC/pycracks/commit/d5c0f5522497df44c58fd574d1cdb53629d4e05d))

* fix(cicd): give write-all permissions ([`d863acc`](https://github.com/ELC/pycracks/commit/d863acc8ab23cf7aa923f184e4bf8b736ff25ca4))

* fix(cicd): add pull-request write permision ([`d4f498a`](https://github.com/ELC/pycracks/commit/d4f498aaa1f3eac446e42b18ccd26a362c6af013))

* fix(cicd): use proper static variable names ([`4d74f2d`](https://github.com/ELC/pycracks/commit/4d74f2d662c30ad99731345f341166df6af4c019))

* fix(cicd): use attached HEAD ([`59008aa`](https://github.com/ELC/pycracks/commit/59008aa485f9f54a046f7ae13c2170823b91e00c))

* fix(cicd): run pipeline on PRs ([`ca3f124`](https://github.com/ELC/pycracks/commit/ca3f12455c0ca1c96f0d22f07606592e5f09293a))

* fix(cicd): add test-finish step ([`0e06d21`](https://github.com/ELC/pycracks/commit/0e06d219280ea572e97871372d194c6887e3aed5))

* fix(cicd): remove manual file specification in coveralls ([`2c7d4f9`](https://github.com/ELC/pycracks/commit/2c7d4f99738f4558d11ef61480c9935cfa10a57c))

* fix: use official coveralls action ([`371b582`](https://github.com/ELC/pycracks/commit/371b582212467270f40b246ac5726199d87ea7df))

* fix(cicd): test alternative test reporter ([`85c710e`](https://github.com/ELC/pycracks/commit/85c710ecb96c0ff6d78748eb33bb0626cedbea60))

* fix(cid): modify permisisons ([`441332b`](https://github.com/ELC/pycracks/commit/441332b7b66ee0cd93437342c7d86fcfdc7db777))

* fix(cicd): only run deploy on master ([`9415da9`](https://github.com/ELC/pycracks/commit/9415da9f50abb4e39a2595eef81f557d0828c3ee))

* fix(cicd): use test reporter with JUnit ([`4122c1f`](https://github.com/ELC/pycracks/commit/4122c1f485aade954625df7d4d9682e7c486c202))

* fix(cicd): cancell previous run on new commits ([`4776e40`](https://github.com/ELC/pycracks/commit/4776e40b559cfbcc5b452b1bc0e183fd1d3cd7fd))

* fix(cicd): use global write permissions for pull-requests ([`94b92dc`](https://github.com/ELC/pycracks/commit/94b92dcca5bf917fd5d134e691323cdaf0c7560c))

* fix(cicd): give write-all permissions ([`1c4d175`](https://github.com/ELC/pycracks/commit/1c4d175791f2c7a1bc89c7a9a75eb0c50dcda659))

* fix(cicd): add pull-request write permision ([`fae952c`](https://github.com/ELC/pycracks/commit/fae952c33b47895b6ecd05246b258df3547bc1c4))

* fix(cicd): use proper static variable names ([`ca7b6fa`](https://github.com/ELC/pycracks/commit/ca7b6fa6c28bf96bbab4474724d7a6f2bcc353cc))

* fix(cicd): use attached HEAD ([`47c5184`](https://github.com/ELC/pycracks/commit/47c51845122e697d50a80ff9a46f8fc9958d103a))

* fix(cicd): run pipeline on PRs ([`69c3758`](https://github.com/ELC/pycracks/commit/69c375835a061671e465e6c4e0e8b2a89fd7489f))

* fix(cicd): use different coverage reporter ([`dff26e4`](https://github.com/ELC/pycracks/commit/dff26e44cb026c941214f52cfe9232a3f1a94e45))


## v0.10.0 (2023-11-11)

### Feature

* feat: install dependencies before checking ([`cd18778`](https://github.com/ELC/pycracks/commit/cd187780ed5eecd30b31f03db16152668b5a9c83))

* feat: add breaking change detection to CICD ([`2177f6c`](https://github.com/ELC/pycracks/commit/2177f6cae696b83d7fdef6d5d53425aadba80b79))

### Fix

* fix: use typing for built in tuple ([`8fd17ea`](https://github.com/ELC/pycracks/commit/8fd17ea78c2419aaac5b96f95706af499c56982c))

* fix(compatibility): use typing_extensions to support Python 3.8 ([`f78080a`](https://github.com/ELC/pycracks/commit/f78080af550d0baab2bf7915dd1b967f30c36c67))

* fix: use local version to check breaking changes ([`56323fc`](https://github.com/ELC/pycracks/commit/56323fc965b0c75ecfbb8bdc23f8562ca28a12e6))


## v0.9.0 (2023-11-07)

### Feature

* feat: add pre-commit check to CICD ([`3c38ac6`](https://github.com/ELC/pycracks/commit/3c38ac687b20c89da6c1ee2da7399c5459655a70))


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
