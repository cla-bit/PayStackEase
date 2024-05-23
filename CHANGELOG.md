# CHANGELOG



## v2.1.0 (2024-05-23)

### Feature

* feat: Added class PayStackWebhook in the webhook module
feat: Added class PayStackSignature in the webhook module
feat: Added custom exception: PayStackServerError, PayStackSignatureVerifyError, APIConnectionError in the api_errors module.
fix: Improved error handling and display user friendly errors to all error classes in the api_errors module.
fix: Added custom exceptions to the SyncBaseClientAPI and AsyncBaseClientAPI classes
fix: Added test for webhook. ([`4dcdb2f`](https://github.com/cla-bit/PayStackEase/commit/4dcdb2fe68cf2a763d9929a719e29cec45393060))

### Fix

* fix: CI/CD workflow ([`6de30bf`](https://github.com/cla-bit/PayStackEase/commit/6de30bf8fa3bb94e3f443a8014a29f9f77c16a1f))

* fix: CI/CD workflow ([`fb08087`](https://github.com/cla-bit/PayStackEase/commit/fb0808753304758e7c94f7e0badbd928c56c3fb7))

### Test

* test: Added more tests functions for webhook module.
test: Updated the test_get_event_data_valid function. ([`ce171b5`](https://github.com/cla-bit/PayStackEase/commit/ce171b5397f3c855412daf370fab6d1e11b5c0e3))

### Unknown

* Merge branch &#39;refs/heads/dev&#39; ([`696c2cb`](https://github.com/cla-bit/PayStackEase/commit/696c2cb3f21cfe33358e67f5cc796b8df765a03d))

* Update test_webhook.py ([`61eeb5f`](https://github.com/cla-bit/PayStackEase/commit/61eeb5f69388c56e08266a68e0beed6350a832b2))

* Update test_webhook.py ([`cf8178d`](https://github.com/cla-bit/PayStackEase/commit/cf8178d74625c09f420f4edd4c848499301a8151))

* Update test_webhook.py ([`cb2dd69`](https://github.com/cla-bit/PayStackEase/commit/cb2dd69c8d4bd148f1088f066eb109395f812b23))

* Update test_webhook.py ([`fff089e`](https://github.com/cla-bit/PayStackEase/commit/fff089e4166d392e5c6bc1d22d589d4dd00b9fa2))

* Update test_webhook.py ([`9baa0fd`](https://github.com/cla-bit/PayStackEase/commit/9baa0fd08c696291bc7bf840a038e1cd77f00e4c))

* Merge pull request #11 from cla-bit/dev

fix: Remove the secret key parameter to avoid overriding. ([`0589159`](https://github.com/cla-bit/PayStackEase/commit/0589159d61571233914baa378c3334ce36c871e8))


## v2.0.4 (2024-05-01)

### Fix

* fix: CI/CD workflow ([`b8d6b38`](https://github.com/cla-bit/PayStackEase/commit/b8d6b38182bc6855fb28904bad3ff76cba25ee24))

### Unknown

* Merge remote-tracking branch &#39;origin/main&#39; ([`99f9475`](https://github.com/cla-bit/PayStackEase/commit/99f94754516a88489927d7c3a8aa23e78267fbce))


## v2.0.3 (2024-05-01)

### Fix

* fix: CI/CD workflow ([`c517dac`](https://github.com/cla-bit/PayStackEase/commit/c517dacf292f8d248c5401203e08b66eddfe9a1b))

### Style

* style: CI/CD workflow ([`8ed7308`](https://github.com/cla-bit/PayStackEase/commit/8ed7308c8f06b9c7a07988fc6b470e9def5ebbb4))

* style: CI/CD workflow ([`f39ac5d`](https://github.com/cla-bit/PayStackEase/commit/f39ac5d6ef63eece846f10820bd46502339b4e63))

* style: CI/CD workflow ([`8af1f69`](https://github.com/cla-bit/PayStackEase/commit/8af1f6990d3c3b1e3b96a01bb9db7d75a667d082))

* style: CI/CD workflow ([`9c6663a`](https://github.com/cla-bit/PayStackEase/commit/9c6663a9be36b08eb25267175fe93ee1fd293561))

* style: CI/CD workflow ([`86e708f`](https://github.com/cla-bit/PayStackEase/commit/86e708f441eb5a0818e0fa459356c60c82a66455))

* style: CI/CD workflow ([`f2842cb`](https://github.com/cla-bit/PayStackEase/commit/f2842cb61791fa9334cad8b0743de58dc2a27063))

* style: updated the CI/CD workflow ([`d8b3227`](https://github.com/cla-bit/PayStackEase/commit/d8b3227a7884218003bd641918efe79f26bda521))

### Unknown

* Merge remote-tracking branch &#39;origin/master&#39; ([`768436c`](https://github.com/cla-bit/PayStackEase/commit/768436cdf2d250c31a7a5c0d2367843bcb58f1b3))


## v2.0.2 (2024-05-01)

### Fix

* fix(package): PayStackError class to return informative error message and status code ([`8d31938`](https://github.com/cla-bit/PayStackEase/commit/8d319381563103def4099135f888797ab514b0cc))

### Unknown

* Merge remote-tracking branch &#39;origin/master&#39;

# Conflicts:
#	CHANGELOG.md ([`3622d97`](https://github.com/cla-bit/PayStackEase/commit/3622d979d0693040b3db82c6f94b09c387430e1e))


## v2.0.1 (2024-05-01)

### Fix

* fix(package): PayStackError class to return informative error message and status code ([`bb44d4c`](https://github.com/cla-bit/PayStackEase/commit/bb44d4c53832b2041ae4b78b4886be4ef4ebb770))

* fix(package): PayStackError class to return informative error message and status code ([`33ec237`](https://github.com/cla-bit/PayStackEase/commit/33ec237686eb6e87168834951aa4407c7d245d25))

### Style

* style(package): updated paystackease-ci-cd yml file ([`81136ad`](https://github.com/cla-bit/PayStackEase/commit/81136ad5ef5138915fc79bc41cd13656d9ebe4ab))

* style(package): updated paystackease-ci-cd yml file ([`83ae0a0`](https://github.com/cla-bit/PayStackEase/commit/83ae0a042864b40521ee65ff4691eaaaca2ebad5))

* style(package): updated paystackease-ci-cd yml file ([`0679f1e`](https://github.com/cla-bit/PayStackEase/commit/0679f1e5c77ddc218f05ae31723bf8614f7de3de))

* style(package): updated paystackease-ci-cd yml file ([`711ed90`](https://github.com/cla-bit/PayStackEase/commit/711ed9014c1b17307dbdb37ed1fc450bea20b349))

* style(package): updated paystackease-ci-cd yml file ([`18ddb8d`](https://github.com/cla-bit/PayStackEase/commit/18ddb8da2c2f51359dfef8d01fe6c4760a962379))

* style(package): updated paystackease-ci-cd yml file ([`dbe5b10`](https://github.com/cla-bit/PayStackEase/commit/dbe5b10b1353c77805aea933403eddfa61a79b5d))

* style(package): updated paystackease-ci-cd yml file ([`3514e7a`](https://github.com/cla-bit/PayStackEase/commit/3514e7a2b676e0009c99a85f26ab4d51b1e8251f))

* style(package): updated paystackease-ci-cd yml file ([`93a50af`](https://github.com/cla-bit/PayStackEase/commit/93a50af3b7c72021ac011654089ebb12fe3bdc7d))

* style(package): updated paystackease-ci-cd yml file ([`abc2a44`](https://github.com/cla-bit/PayStackEase/commit/abc2a4424ef178a7c78a81aabb036d99ade8892f))

* style(package): updated paystackease-ci-cd yml file ([`4785cf9`](https://github.com/cla-bit/PayStackEase/commit/4785cf90397a28b38b9aaf589d947769aa3928e7))

* style(package): updated paystackease-ci-cd yml file ([`4c7dd94`](https://github.com/cla-bit/PayStackEase/commit/4c7dd944ccae21a43c17b99a8fc9a51a03d6dfe1))

* style(package): updated paystackease-ci-cd yml file ([`fced90f`](https://github.com/cla-bit/PayStackEase/commit/fced90f0402beba14e68b2be983adafafc7e7da0))

* style(package): updated paystackease-ci-cd yml file ([`48c13e5`](https://github.com/cla-bit/PayStackEase/commit/48c13e5e8046518bfa40d7b44a9c977e156b1c1f))

* style(package): updated paystackease-ci-cd yml file ([`c2d7a4c`](https://github.com/cla-bit/PayStackEase/commit/c2d7a4cf0927ea530a30273ae0002f30d8da51a6))

* style(package): updated paystackease-ci-cd yml file ([`3f8c691`](https://github.com/cla-bit/PayStackEase/commit/3f8c691313dc1a2e85772b8c271a05c44829eaa2))

* style(package): updated paystackease-ci-cd yml file ([`0d02a50`](https://github.com/cla-bit/PayStackEase/commit/0d02a5024a609c85ab304ed050b7932706a9abc5))

* style(package): updated paystackease-ci-cd yml file ([`b63edb2`](https://github.com/cla-bit/PayStackEase/commit/b63edb2d5f585d28a0edeff1eff2ea40c1d08d98))

* style(package): updated paystackease-ci-cd yml file ([`ce34905`](https://github.com/cla-bit/PayStackEase/commit/ce349055ffb51663bb35590c9aeb11e295877c7f))

* style(package): updated paystackease-ci-cd yml file ([`7e2de77`](https://github.com/cla-bit/PayStackEase/commit/7e2de77c86c1d99839bbaf33d39ff91caa72aac7))

* style(package): updated paystackease-ci-cd yml file ([`edbdfe4`](https://github.com/cla-bit/PayStackEase/commit/edbdfe42e44ba4f8612f3dd8e332b5d30fca6b90))

* style(package): updated paystackease-ci-cd yml file ([`e9e9cd3`](https://github.com/cla-bit/PayStackEase/commit/e9e9cd3cb30d152077a4a7e6e1cbf14f0a127aec))

* style(package): updated paystackease-ci-cd yml file ([`436af59`](https://github.com/cla-bit/PayStackEase/commit/436af591f667e5de8902338a9e6ea0ba691883ff))

* style(package): updated paystackease-ci-cd yml file ([`5a7a6b3`](https://github.com/cla-bit/PayStackEase/commit/5a7a6b34658a7e42d136b461af859b95d540c47e))

* style(package): updated paystackease-ci-cd yml file ([`a8f39b9`](https://github.com/cla-bit/PayStackEase/commit/a8f39b9eda8dc633fc83db8a42b779b88dc8c7df))

* style(package): updated pyproject toml file ([`153a589`](https://github.com/cla-bit/PayStackEase/commit/153a58962b17fd901657765f53e5b119a6606d96))

* style(package): updated paystackease-ci-cd yml file ([`ef35fa8`](https://github.com/cla-bit/PayStackEase/commit/ef35fa8088a31a47b6749eac05f473d25478092c))

* style(package): added pyptoject ([`941cd9b`](https://github.com/cla-bit/PayStackEase/commit/941cd9b2cb1026b832eb9d79c49d9a8563022a13))

* style(package): added PSR ([`3280a6b`](https://github.com/cla-bit/PayStackEase/commit/3280a6ba616a1baf36789151e29a6d1518c7cbc1))

### Unknown

* Merge remote-tracking branch &#39;origin/master&#39; ([`344ea0c`](https://github.com/cla-bit/PayStackEase/commit/344ea0cc3379c7053639ef0f778857bc6d214931))

* added paystackease CI workflow ([`667510d`](https://github.com/cla-bit/PayStackEase/commit/667510d8f28b4fb7c95ae2f508e15f128bd28a94))

* added paystackease CI workflow ([`4dd207c`](https://github.com/cla-bit/PayStackEase/commit/4dd207c501d51673945634787b87bea3b3643269))

* added paystackease CI workflow ([`773b34e`](https://github.com/cla-bit/PayStackEase/commit/773b34ef27081adc095050c4255d72acdf494c07))

* added paystackease CI workflow ([`0e13432`](https://github.com/cla-bit/PayStackEase/commit/0e13432415fbc6eef7b84f2f9e79700cd498480f))

* added paystackease CI workflow ([`63d32d3`](https://github.com/cla-bit/PayStackEase/commit/63d32d30a35c0e5974716ad9efeeb6a75d36ffbd))

* updated tests ([`c9ea929`](https://github.com/cla-bit/PayStackEase/commit/c9ea92960e0bd3582951df599b6d39a74ba60694))

* updated pyproject file ([`b5560c8`](https://github.com/cla-bit/PayStackEase/commit/b5560c86b29a4d58977b97a2c79941728d92cf6c))

* added version ([`530c367`](https://github.com/cla-bit/PayStackEase/commit/530c367ad09adfddc90841d942e076b10e809a61))

* Update index.rst ([`2ebdb5c`](https://github.com/cla-bit/PayStackEase/commit/2ebdb5c4c2b8222b7f37d9dbf7f4e14357a643bb))

* fixed the message and status_code in PayStackError class ([`d8b655d`](https://github.com/cla-bit/PayStackEase/commit/d8b655dab28b9117353d2e7bf67c0d631872879b))

* updated ([`4528159`](https://github.com/cla-bit/PayStackEase/commit/452815999d8bd8f7af87d8c415b4e2f469792183))


## v2.0.0 (2024-04-19)

### Unknown

* updated ([`4035650`](https://github.com/cla-bit/PayStackEase/commit/40356501e16379217b5ba7f52f3efac9e56ddd77))

* updated ([`f0629a7`](https://github.com/cla-bit/PayStackEase/commit/f0629a7418547814d2d058ef07a44411a5ca173c))

* updated ([`8fa7d3f`](https://github.com/cla-bit/PayStackEase/commit/8fa7d3f252ccc99edc2e2e35afdfec605d16cd76))

* updated ([`259d8aa`](https://github.com/cla-bit/PayStackEase/commit/259d8aa63839e545f86a4f988dea2b343bb2a01f))

* updated documentation ([`681ef40`](https://github.com/cla-bit/PayStackEase/commit/681ef4030fe460817dff2e361c654822e60c314d))

* updated documentation ([`df4fe69`](https://github.com/cla-bit/PayStackEase/commit/df4fe696aa1d378013dff7ece199e976909491f5))

* improved error handling ([`2403672`](https://github.com/cla-bit/PayStackEase/commit/24036725e657f33de969d6b1419eb8c0fd4738c7))

* improved error handling ([`daa075b`](https://github.com/cla-bit/PayStackEase/commit/daa075bd10471d88c43a025576258966997b7ca6))

* updated documentations ([`acbdb48`](https://github.com/cla-bit/PayStackEase/commit/acbdb48c21fa562803f96abbdab1e8720e521e4d))

* updated tests ([`26e31fe`](https://github.com/cla-bit/PayStackEase/commit/26e31feabfb8143ae7888f34b9e6de6d2cbdf45d))

* updated ([`28a6d28`](https://github.com/cla-bit/PayStackEase/commit/28a6d282c3d43eb32c1a251796ced2b5ad69843f))

* updated ([`d2de289`](https://github.com/cla-bit/PayStackEase/commit/d2de289508ee706fb11cad5c095dc8c5fd573237))

* updated tests ([`244d940`](https://github.com/cla-bit/PayStackEase/commit/244d9407234f588eba08930358940de46836aff4))

* updated ([`055e43c`](https://github.com/cla-bit/PayStackEase/commit/055e43cdbc9c9e3d523d7f2d9b57929c535a66ed))

* updated tests ([`f6356de`](https://github.com/cla-bit/PayStackEase/commit/f6356de80928bdfe6356b51823ef19b7ecc0eec6))

* updated the design pattern and structure ([`4a6f531`](https://github.com/cla-bit/PayStackEase/commit/4a6f531ba20acc552e09bf3fea7a356e44ced26b))

* updated the design pattern and structure ([`41ef129`](https://github.com/cla-bit/PayStackEase/commit/41ef129b73878e4e5fb64d6b68aa950cd53e94c2))

* updated ([`389d74e`](https://github.com/cla-bit/PayStackEase/commit/389d74ec53f983c137f9b0df29c163c4c7f90992))

* updated ([`0a73514`](https://github.com/cla-bit/PayStackEase/commit/0a735148dec8df8aa872e78492f220d261645488))

* updated tests ([`2b7f2b1`](https://github.com/cla-bit/PayStackEase/commit/2b7f2b16c17b4383a1068d0e4d1a0733a8c4b73f))

* updated the object name from Response to PayStackResponse. ([`8196a57`](https://github.com/cla-bit/PayStackEase/commit/8196a57f518b00ec421e425978336d9ad600f3a5))

* improved the Response object ([`85b4ca8`](https://github.com/cla-bit/PayStackEase/commit/85b4ca857792e96b43915976f2d086daa23eec54))

* created separate folders for sync and async api requests ([`1db0f4d`](https://github.com/cla-bit/PayStackEase/commit/1db0f4df0a2a94c89e4659310a37e02905307ff2))

* updated documentation. ([`2cb2f8e`](https://github.com/cla-bit/PayStackEase/commit/2cb2f8e408c70a0e3262b058b41e867ef81b3b52))

* updated documentation: install ([`6cc54e4`](https://github.com/cla-bit/PayStackEase/commit/6cc54e4b8ffbde6b16248a9d80aed4192524b22b))

* updated documentation: example ([`dcc91e1`](https://github.com/cla-bit/PayStackEase/commit/dcc91e16e9b52d7ceab1cf327229e99446def16d))

* updated index and conf files documentation. ([`d8b597a`](https://github.com/cla-bit/PayStackEase/commit/d8b597a7b0363a3a40738e74608e76362fd0e6f0))

* updated changelog documentation. ([`031701d`](https://github.com/cla-bit/PayStackEase/commit/031701d21c69d1c815e2f0ef361a99cb53711b4a))

* updated poetry lock file ([`54f93d9`](https://github.com/cla-bit/PayStackEase/commit/54f93d9622cd45f834a67366c85eb0156e04c5ab))

* updated ([`855476e`](https://github.com/cla-bit/PayStackEase/commit/855476e8bcb8e267e6b43014bbb1ca4003532511))

* updated ([`aafb09c`](https://github.com/cla-bit/PayStackEase/commit/aafb09c22884b268371457ac71d96eaf43deee31))

* updated changelog file ([`330e900`](https://github.com/cla-bit/PayStackEase/commit/330e900b709ecec6a565bc20b3c28e663a87b5ae))

* updated the type hint ([`cc53290`](https://github.com/cla-bit/PayStackEase/commit/cc532906d033be72b45ee3de943b50ba7e666387))

* updated ([`82d3147`](https://github.com/cla-bit/PayStackEase/commit/82d314793462f3c9a8686ded6a5e89d5fb5b950c))

* updated ([`212e06a`](https://github.com/cla-bit/PayStackEase/commit/212e06aca903a5c6b04d0527ce68123ca203c842))

* updated ([`0744b59`](https://github.com/cla-bit/PayStackEase/commit/0744b594068dbadb296a9855bc47e6f4b7fa32f0))

* updated poetry lock file and changelog file ([`72ef7c7`](https://github.com/cla-bit/PayStackEase/commit/72ef7c72e0b7a797aa0b61f32e8010c6da075b5c))


## v1.0.0 (2024-04-05)

### Unknown

* updated pyproject and readme ([`f85a2de`](https://github.com/cla-bit/PayStackEase/commit/f85a2def099ecf3c8e23d9203c3b4a4e69013b26))

* fixed type hint issue ([`42add51`](https://github.com/cla-bit/PayStackEase/commit/42add51cc81a90ae565f8f1096f684dcbb4bf76d))

* fixed type hint issue ([`a8bd30d`](https://github.com/cla-bit/PayStackEase/commit/a8bd30d62887169a9e79939be626034cdf3086de))

* fixed type hint issue ([`119bce8`](https://github.com/cla-bit/PayStackEase/commit/119bce843d9222f563f867f1b3b8a5bc6de51d27))

* updated ([`39db5d3`](https://github.com/cla-bit/PayStackEase/commit/39db5d3b45ebb272eefb82a4b5c1f47a93acbf06))

* fixed type hint issue ([`816a35d`](https://github.com/cla-bit/PayStackEase/commit/816a35daf1d3d4b58c29624adfbe806344868123))

* fixed type hint issue ([`eed8658`](https://github.com/cla-bit/PayStackEase/commit/eed86587cf191854e5a5b8fc62815640f23a41f4))

* updated ([`063c594`](https://github.com/cla-bit/PayStackEase/commit/063c59414f3f744276483faff73ef270a35be3e5))

* fixed type hint issue ([`2bc112a`](https://github.com/cla-bit/PayStackEase/commit/2bc112a1fded75983a0fa601513bfa5716c16bf3))

* fixed type hint issue ([`a879f1b`](https://github.com/cla-bit/PayStackEase/commit/a879f1b709bfe5310633c867ed6f26cbbbfe745d))

* fixed value issue. ([`cff893f`](https://github.com/cla-bit/PayStackEase/commit/cff893f088d73e45d768a5d9dc61379172fe7687))

* fixed type hint issue. ([`82b4e7c`](https://github.com/cla-bit/PayStackEase/commit/82b4e7c61bf4248b787669adb84a8b5bdbed24f1))

* fixed type hint issue. ([`3f1f465`](https://github.com/cla-bit/PayStackEase/commit/3f1f465c350cff1de9d570033dd930e549395ff3))

* fixed type hint issue. ([`7e82c64`](https://github.com/cla-bit/PayStackEase/commit/7e82c64ad84be01f27e9cb6a371162320d6dc0c6))

* fixed type hint issue. ([`cfcfe46`](https://github.com/cla-bit/PayStackEase/commit/cfcfe46d19f26a29cfd67f75cbd75364174cc575))

* fixed type hint issue. ([`c9ff2e2`](https://github.com/cla-bit/PayStackEase/commit/c9ff2e22d1e5dd9004624e9b6f4a2a5e5798dc68))

* fixed type hint issue. ([`98da188`](https://github.com/cla-bit/PayStackEase/commit/98da1886cdf15cac5f3f543d3bbe94ae2cecae43))

* removed json import ([`e6fef1c`](https://github.com/cla-bit/PayStackEase/commit/e6fef1c7c55b62cbbc1c0a9fe0d3086c66f694af))

* fixed the Response return type ([`c6a0b3f`](https://github.com/cla-bit/PayStackEase/commit/c6a0b3fb127097afff6280744411ac5c339debc8))

* formatted with pylint and black ([`3585051`](https://github.com/cla-bit/PayStackEase/commit/358505193c1facc95c81b548cd326c54597e7141))

* formatted with pylint and black ([`9bcfe14`](https://github.com/cla-bit/PayStackEase/commit/9bcfe14b5bb8cf1eeae55eabffbd6ba6c0f5b261))

* changed the Response type to the response from Paystack server. ([`5dff180`](https://github.com/cla-bit/PayStackEase/commit/5dff180f3d69ec21b62ab09a7c89a5375ada36d1))

* added a utils file ([`23fc48c`](https://github.com/cla-bit/PayStackEase/commit/23fc48c1ee71239f493f1b609a45af0fd9e922b7))


## v0.1.3 (2024-04-04)

### Unknown

* updated tests for verification: async and sync ([`77edffe`](https://github.com/cla-bit/PayStackEase/commit/77edffec4f82999fc65c67f41bf34bbaa0551e31))

* updated te return type from dict to Response and ClientResponse object respectively. ([`e4cca50`](https://github.com/cla-bit/PayStackEase/commit/e4cca502335e37b83685fdd3b3c6cfd5cdb0184a))

* updated te return type from dict to Response and ClientResponse object respectively. ([`0134ce6`](https://github.com/cla-bit/PayStackEase/commit/0134ce65746a2b9116d16fd1f1acf9504585455c))

* updated documentation for transfers control: async and sync ([`072bd07`](https://github.com/cla-bit/PayStackEase/commit/072bd07b328a0813d4c24eb43f585b49fa40082a))

* updated documentation for transfer: async and sync ([`8645152`](https://github.com/cla-bit/PayStackEase/commit/8645152eb36c7a34ff16691c93da7cc2ed43a9e0))

* updated te return type from dict to Response and ClientResponse object respectively. ([`d545ba4`](https://github.com/cla-bit/PayStackEase/commit/d545ba4f5292fbd9157e97188b295ca079494351))

* updated te return type from dict to Response and ClientResponse object respectively. ([`72f1057`](https://github.com/cla-bit/PayStackEase/commit/72f1057a356e9c3086365b14e571ca554bf52e66))

* updated documentation for transfer recipients: async and sync ([`ed9e357`](https://github.com/cla-bit/PayStackEase/commit/ed9e357623e63afb06de7e8000cb215f28e400ea))

* updated documentation for transaction splits: async and sync ([`c86d5be`](https://github.com/cla-bit/PayStackEase/commit/c86d5be6edf793d8b47535ec3fc1a5871d2a2285))

* updated tests for transaction splits: async and sync ([`cfddbed`](https://github.com/cla-bit/PayStackEase/commit/cfddbedeb11dd9682018604e8fbb43cf791e4349))

* updated te return type from dict to Response and ClientResponse object respectively. ([`cfb089a`](https://github.com/cla-bit/PayStackEase/commit/cfb089a49d2e7763566d8cb7e801bbd4d100cd79))

* updated te return type from dict to Response and ClientResponse object respectively. ([`3bbf976`](https://github.com/cla-bit/PayStackEase/commit/3bbf976c2808e47f47a40857014aa2d8e05b464b))

* updated test for transaction: async and sync ([`f807ede`](https://github.com/cla-bit/PayStackEase/commit/f807ede122572020505201992a7080e7f97d7638))

* updated documentation for transaction: async and sync ([`4057d77`](https://github.com/cla-bit/PayStackEase/commit/4057d7781c60506af2beb2ece7aa010cb464d8fb))

* added TransactionStatus enum class ([`974e4b3`](https://github.com/cla-bit/PayStackEase/commit/974e4b33781e530bc6e3957405cd2b35a5903288))

* added Bearer enum class ([`2e5611a`](https://github.com/cla-bit/PayStackEase/commit/2e5611affd3c095f76d34909fda0f2db5044da0e))

* updated te return type from dict to Response and ClientResponse object respectively. ([`30216d1`](https://github.com/cla-bit/PayStackEase/commit/30216d1a8a753375d2884c500ae648becd007191))

* updated documentation for terminals: sync and async ([`ca6d1ad`](https://github.com/cla-bit/PayStackEase/commit/ca6d1ad9719afbd2cef494e1084f06f2def6a7d2))

* added event action enum class ([`566035b`](https://github.com/cla-bit/PayStackEase/commit/566035b23b2e551c853cddc771c33e9ab8889fa4))

* updated test for terminal: async and sync ([`872ef2b`](https://github.com/cla-bit/PayStackEase/commit/872ef2b4d86246cec09742121b162633e0a63584))

* updated documentation for subscriptions: async and sync ([`71b9173`](https://github.com/cla-bit/PayStackEase/commit/71b91731d78e1bfafaeb5319c4c7bc5fef5aca25))

* updated te return type from dict to Response and ClientResponse object respectively. ([`d47783a`](https://github.com/cla-bit/PayStackEase/commit/d47783a5639bfd89a78ca242b76946cd306f490b))

* updated te return type from dict to Response and ClientResponse object respectively. ([`887d232`](https://github.com/cla-bit/PayStackEase/commit/887d23224bf2554cd353940499ba7ae2f47863f3))

* updated documentation for subaccounts: async and sync ([`0b81c83`](https://github.com/cla-bit/PayStackEase/commit/0b81c832c6150953c68ac04cfa84eee254707747))

* updated tests for subaccounts: async and sync ([`c5bc212`](https://github.com/cla-bit/PayStackEase/commit/c5bc21226a9bc457ba11472f88cc6050f356dbec))

* added a settlement schedule enum class ([`ac94065`](https://github.com/cla-bit/PayStackEase/commit/ac94065c2290875f8069c7759a5004689d96645e))

* updated te return type from dict to Response and ClientResponse object respectively. ([`b2e3cf5`](https://github.com/cla-bit/PayStackEase/commit/b2e3cf595be919cffc07be665bb0220e3d704e8b))

* updated status enum class ([`7e3261d`](https://github.com/cla-bit/PayStackEase/commit/7e3261d9be21cf16eeb8da1bf2a6f06642f948c2))

* updated tests for settlements: async and sync ([`4205bbb`](https://github.com/cla-bit/PayStackEase/commit/4205bbb29ae76d4277438729b8e0dcce23b39b51))

* updated documentation for settlements: async and sync ([`9aaa3d6`](https://github.com/cla-bit/PayStackEase/commit/9aaa3d6459f978c351bd18bfc3f96934ab89240d))

* updated documentation for refund: async and sync ([`bf7957f`](https://github.com/cla-bit/PayStackEase/commit/bf7957fb4298daafcd988b02447fba3aa89fc7dd))

* updated documentation for refund: async and sync ([`f8a4531`](https://github.com/cla-bit/PayStackEase/commit/f8a453171accdc6d201f6357d7e3fd1ef9e174a2))

* updated te return type from dict to Response and ClientResponse object respectively. ([`1b5de71`](https://github.com/cla-bit/PayStackEase/commit/1b5de7156a6432beb3159a0350ebee65c10c7d97))

* updated te return type from dict to Response and ClientResponse object respectively. ([`3627aa0`](https://github.com/cla-bit/PayStackEase/commit/3627aa0bbbeef83649abf82447d59808aedba588))

* updated documentation for products: async and sync ([`ff8cd29`](https://github.com/cla-bit/PayStackEase/commit/ff8cd29dd1ab09e2615072ac4d72bfc598f998b9))

* updated tests for products: async and sync ([`8d35f91`](https://github.com/cla-bit/PayStackEase/commit/8d35f918519b4b0bf5cbb4972520b2b20130eb14))

* updated tests for plan: async and sync ([`ce0ce5c`](https://github.com/cla-bit/PayStackEase/commit/ce0ce5ca022b7145ed7a7909f441d4c526560ba5))

* updated documentation for plan: async and sync ([`cb7b96b`](https://github.com/cla-bit/PayStackEase/commit/cb7b96b0068a5f0318bc990fdd6e35ebe31e4c9c))

* updated te return type from dict to Response and ClientResponse object respectively. ([`e954e7e`](https://github.com/cla-bit/PayStackEase/commit/e954e7e208c7f3a292ada76beaa40a7b77b0fb32))

* updated te return type from dict to Response and ClientResponse object respectively. ([`9d94d2d`](https://github.com/cla-bit/PayStackEase/commit/9d94d2d4811835d50be453011fc29abb7968cba6))

* added a PayMentRequestStatus enum class ([`447ae75`](https://github.com/cla-bit/PayStackEase/commit/447ae7517870532a76cd9edbcb3b4aa771f86219))

* updated documentation for payment requests: async and sync ([`1fc8bd6`](https://github.com/cla-bit/PayStackEase/commit/1fc8bd6a03ee66a72fb8eca842fd2523874e2f45))

* updated test for payment requests: async and sync ([`5dde4db`](https://github.com/cla-bit/PayStackEase/commit/5dde4db18eada947dd922b82af3a196a09388d66))

* updated test for payment pages: async and sync ([`16319fd`](https://github.com/cla-bit/PayStackEase/commit/16319fd717720892bb28c3beb57559947a0b453e))

* updated te return type from dict to Response and ClientResponse object respectively. ([`c88660d`](https://github.com/cla-bit/PayStackEase/commit/c88660d434f064145f8a106ee1b7481cbc17b6d3))

* updated documentation payment pages: async and sync ([`f11cc92`](https://github.com/cla-bit/PayStackEase/commit/f11cc92c764d2a93449b65e85ad10f3dfbc3dbb5))

* updated typing annotations ([`b8fdd00`](https://github.com/cla-bit/PayStackEase/commit/b8fdd00df4c1a9eebfd277d53d14316595ebaf87))

* updated errors for testing ([`743a4ef`](https://github.com/cla-bit/PayStackEase/commit/743a4ef7f7e7165de58b8c180a4bb1ac70c27423))

* Merge remote-tracking branch &#39;origin/master&#39; ([`da07720`](https://github.com/cla-bit/PayStackEase/commit/da077204fbd3a83b3851b3ee5c35d10726470b16))

* updated the typing annotations for base and abase scripts ([`2089e40`](https://github.com/cla-bit/PayStackEase/commit/2089e403461d7c90cfd79c9dfbd1aa8e004b3978))

* Update charges.rst ([`b3fb72d`](https://github.com/cla-bit/PayStackEase/commit/b3fb72de076c2fae7dcce5242b6042c39807e843))

* Update acharges.rst ([`f528c8a`](https://github.com/cla-bit/PayStackEase/commit/f528c8abcc2cf3e0c1dac9e7bdd81fc7bf592375))

*  updated te return type from dict to Response and ClientResponse object respectively. ([`e3eec87`](https://github.com/cla-bit/PayStackEase/commit/e3eec8737cdecd3e80c43c50f7466e9db4b7e9c4))

* updated documentation for miscellaneous: async and sync ([`2b12dab`](https://github.com/cla-bit/PayStackEase/commit/2b12dab718c8c70284d91d69a754ee3e2bd7e470))

* Added gateway enum class ([`76f45ac`](https://github.com/cla-bit/PayStackEase/commit/76f45ac021c186b2ab1e8f822b20f199c56fce95))

* updated documentation of integration: async and sync ([`0fa1f2e`](https://github.com/cla-bit/PayStackEase/commit/0fa1f2e5c89b0e68c11ac8d97cd74acf4e76a8fb))

*  updated te return type from dict to Response and ClientResponse object respectively. ([`7db27de`](https://github.com/cla-bit/PayStackEase/commit/7db27dea4511c21a8ef99e1baf82bca61f3ab67b))

*  updated te return type from dict to Response and ClientResponse object respectively. ([`23f5153`](https://github.com/cla-bit/PayStackEase/commit/23f51531380ef0548a0f1a40a2e962bfd45364e9))

* updated documentation for disputes: async and sync ([`bc1f086`](https://github.com/cla-bit/PayStackEase/commit/bc1f086b47392540a633547b4cef483e74849472))

* updated test for disputes: async and sync ([`ccfd2c4`](https://github.com/cla-bit/PayStackEase/commit/ccfd2c450947f4333d46c58787ca3063022686ad))

* added DisputeStatus enum class ([`4cbb6a2`](https://github.com/cla-bit/PayStackEase/commit/4cbb6a26309976427b1e3615417320775ea85d8e))

*  updated te return type from dict to Response and ClientResponse object respectively. ([`d5e6037`](https://github.com/cla-bit/PayStackEase/commit/d5e60379daea25df43a2494c343f48d732e8840d))

* updated tests for dva: sync and async ([`ef5d2ea`](https://github.com/cla-bit/PayStackEase/commit/ef5d2eaa745dc502d4a00295d3091a79a19e56c0))

* updated documentation for dva: sync and async ([`64c49da`](https://github.com/cla-bit/PayStackEase/commit/64c49dad0ef4132f4c1b421aa52996e92d99f910))

* added DVABank enum class ([`3f4eee8`](https://github.com/cla-bit/PayStackEase/commit/3f4eee86abb7b46d98eb169eb14102d64a334129))

* updated documentation customers: async and sync ([`784b119`](https://github.com/cla-bit/PayStackEase/commit/784b11901ab55d66997d2f9f17a4b21c42297b01))

*  updated te return type from dict to Response and ClientResponse object respectively. ([`6694a61`](https://github.com/cla-bit/PayStackEase/commit/6694a6144d31af6eafb34c38d1f7f184dc98b2b8))

*  updated te return type from dict to Response and ClientResponse object respectively. ([`84786c5`](https://github.com/cla-bit/PayStackEase/commit/84786c51c0057a16cd6e241944b90d96edd34037))

* updated test for charges: async and sync ([`9fcdea5`](https://github.com/cla-bit/PayStackEase/commit/9fcdea56f01188778cf271a5d5802a258ea40e83))

* updated documentation ([`d4b27e0`](https://github.com/cla-bit/PayStackEase/commit/d4b27e01dee71e4919bffa64f416bd16e3a75f1a))

* added EFT enum class ([`8bc4e4a`](https://github.com/cla-bit/PayStackEase/commit/8bc4e4a40c5c9d0eaf6af4a77d59669064d227c4))

* updated documentation charges: async and sync ([`50d6548`](https://github.com/cla-bit/PayStackEase/commit/50d65486b2003b9132705732d042cebb317ca170))

* updated from Union type to Optional ([`f8567fe`](https://github.com/cla-bit/PayStackEase/commit/f8567fe4ca752c624d6c1f7c48a21147c9e48815))

* added Union typE hint and a default value ([`ade0fff`](https://github.com/cla-bit/PayStackEase/commit/ade0fff848c35887906ac57d590c403f3213dcd4))

* updated documentation bulk charges: sync and async ([`b518ce1`](https://github.com/cla-bit/PayStackEase/commit/b518ce16bcb20cef7539715a90a119aa56439202))

* updated te return type from dict to Response and ClientResponse object respectively. ([`45fe4ce`](https://github.com/cla-bit/PayStackEase/commit/45fe4ce294038ae8450102d4699f751a76236fa8))

* updated te return type from dict to Response and ClientResponse object respectively. ([`bcbe10d`](https://github.com/cla-bit/PayStackEase/commit/bcbe10de54bcf4a8a9a1fddfacc8d0c3d3d4e16f))

* updated documentation: applepay and aapplepay ([`854f13f`](https://github.com/cla-bit/PayStackEase/commit/854f13f4edfe4692ab877373e3e1b02adf48de22))

* updated the return type from dict to Response and ClientResponse ([`e466a6a`](https://github.com/cla-bit/PayStackEase/commit/e466a6ae10c2aada078013b845a9d8a7d3420205))

* updated the test: abase and base ([`21769a8`](https://github.com/cla-bit/PayStackEase/commit/21769a863cc9fd11e55f2d4968cf2d5c83f9875d))

* updated the return type from dict to Response and ClientResponse ([`8091f58`](https://github.com/cla-bit/PayStackEase/commit/8091f58af699101ac359c94da224116cff31ab0c))

* removed str(val) from lower case method ([`75df2ae`](https://github.com/cla-bit/PayStackEase/commit/75df2ae4f582cf02db2f0ddc1815f0073a891494))

* removed str(val) from lower case method ([`d1eb571`](https://github.com/cla-bit/PayStackEase/commit/d1eb5719f44dbd7130e18749339ae2077dcf6780))

* Update _abase.py ([`ed9f29c`](https://github.com/cla-bit/PayStackEase/commit/ed9f29cb6dbb9370ceaf0a81e77d23a835f37101))

* Update _base.py ([`9df0067`](https://github.com/cla-bit/PayStackEase/commit/9df0067cf41f6f3248490ecf837448fe13d93b6a))

* updated the following async and sync rst files: customers ([`a8e645f`](https://github.com/cla-bit/PayStackEase/commit/a8e645f46119a9ce810993b3b4c09972640856fc))

* updated the following async and sync rst files: customers ([`3b9fb15`](https://github.com/cla-bit/PayStackEase/commit/3b9fb150af6b5acb45ea2d57a8e1864c6cce4a78))

* updated the following async and sync test py files: customers ([`7eca457`](https://github.com/cla-bit/PayStackEase/commit/7eca457464ad39631002d0fe59d6ab6f6fd2c392))

* updated the following async and sync py files: customers: added default values ([`7a7ccdf`](https://github.com/cla-bit/PayStackEase/commit/7a7ccdf5a846583b269187a792c74fc6f5062813))

* updated the following async and sync py files: customers: added default values ([`b078998`](https://github.com/cla-bit/PayStackEase/commit/b07899861f2e0dcb9471b298ad25ac8608b573c8))

* updated the following async and sync rst files: charges ([`2daa9fb`](https://github.com/cla-bit/PayStackEase/commit/2daa9fb3069a586f6f9fdd6eff36d05eb9c4d040))

* updated the following async and sync test files: charges ([`856ab07`](https://github.com/cla-bit/PayStackEase/commit/856ab07296540aa06051b7b3d37dd3757d2dd506))

* updated the following async and sync rst files: bulk charges ([`2281c4f`](https://github.com/cla-bit/PayStackEase/commit/2281c4fceff3e8bf27a5dbdff7a07bc4a79745b7))

* updated the following async and sync rst files: apple pay ([`8c46230`](https://github.com/cla-bit/PayStackEase/commit/8c46230b36f0c7056232c3363732048693b0c74d))

* updated the following async and sync rst files: apple pay ([`41fa71e`](https://github.com/cla-bit/PayStackEase/commit/41fa71e301b1479579b0b758b5fd8c99d6b789d7))

* updated the following async and sync rst files: bulk charges ([`5c029aa`](https://github.com/cla-bit/PayStackEase/commit/5c029aaf56cd7b12256f407384edbbcd34452a3f))

* updated the following rst files: aapplepay, applepay ([`94037e9`](https://github.com/cla-bit/PayStackEase/commit/94037e910c34eeb5238fbaf925d6bc3ab9aba48a))

* updated the following rst files: submodules ([`1d390ae`](https://github.com/cla-bit/PayStackEase/commit/1d390aeb5d9a7a649466a11ded65d7a38ac0e6d8))

* updated the following rst files: paystack and apaystack ([`cc46c46`](https://github.com/cla-bit/PayStackEase/commit/cc46c464cdfb8be64deeae88da4e64607bce33a9))

* added favicon ([`7d3046f`](https://github.com/cla-bit/PayStackEase/commit/7d3046fb67aa4eb0d60d44571b3647b11215a8d5))

* updated async and sync bulk charges: added default values, Union, removed Optional. ([`300e054`](https://github.com/cla-bit/PayStackEase/commit/300e0549cb08fc400a6438e11f95a02789808b4d))

* updated conf.py: added logo ([`a1cab86`](https://github.com/cla-bit/PayStackEase/commit/a1cab86b8f367961e63cbb800beceb139a356920))

* updated conf.py: added logo ([`575a21a`](https://github.com/cla-bit/PayStackEase/commit/575a21a8dc70a9d1e95f7d551b847dbb0e4df4e4))

* updated readme.md ([`7d28d9b`](https://github.com/cla-bit/PayStackEase/commit/7d28d9b61b98ecefe1a0e7505723859f74c6ce48))

* Delete docs/images/paystackease.png ([`11646b7`](https://github.com/cla-bit/PayStackEase/commit/11646b7409b3fec50f777ec045c984790a32b3d9))

* added paystackease logo ([`7c6bf36`](https://github.com/cla-bit/PayStackEase/commit/7c6bf361e179094a32a5d4cb3c439868a4423a6d))

* added tests for date and datetime for both the async and sync base files ([`d878d5f`](https://github.com/cla-bit/PayStackEase/commit/d878d5fabbd3ac5d18d2ad2328cea191d6f23217))

* Merge remote-tracking branch &#39;origin/master&#39; ([`454e5a7`](https://github.com/cla-bit/PayStackEase/commit/454e5a7c1b0c6dff58ebe2f8b326987288bdb098))

* updated readme ([`891a7f7`](https://github.com/cla-bit/PayStackEase/commit/891a7f7a18baae75b4fe9071043363a907d4e389))

* Delete requirements.txt ([`47ef9ca`](https://github.com/cla-bit/PayStackEase/commit/47ef9caaf87be698524ddbedd5b233a0a6e7a0d2))

* Update .readthedocs.yaml ([`90c3544`](https://github.com/cla-bit/PayStackEase/commit/90c3544071b25693d692bb20d18472cf27e52baf))

* Update .readthedocs.yaml ([`4c54bc0`](https://github.com/cla-bit/PayStackEase/commit/4c54bc08adc065f296e52898f86b57feb3fd4130))

* Update .readthedocs.yaml ([`5fdeb2c`](https://github.com/cla-bit/PayStackEase/commit/5fdeb2c6f22d65304aaefc3cfa8afe6c29b60c55))

* Update .readthedocs.yaml ([`6327a9d`](https://github.com/cla-bit/PayStackEase/commit/6327a9d689859c367328f4a83528fee16adee008))

* Update .readthedocs.yaml ([`9333650`](https://github.com/cla-bit/PayStackEase/commit/93336502bee0d556ab01de3ce096b4574390f838))

* Update .readthedocs.yaml ([`c2b504d`](https://github.com/cla-bit/PayStackEase/commit/c2b504dd79dbc8fb92da35b625e86544954b4189))

* Update changelog.rst ([`fc2a2b4`](https://github.com/cla-bit/PayStackEase/commit/fc2a2b4ff16905535541d1cd0a5f2e847304a059))

* Update conf.py ([`ff1e257`](https://github.com/cla-bit/PayStackEase/commit/ff1e2575cdfb8161530405e878c033fc3e98555f))

* updated pyproject toml file ([`e78a20b`](https://github.com/cla-bit/PayStackEase/commit/e78a20b146907cde492917e471de695f7e439a19))

* updated changelog and readme files ([`f51b8b9`](https://github.com/cla-bit/PayStackEase/commit/f51b8b9d4b9b54d42ef3e3852d621da46a991922))

* updated chanelog and readme files ([`87f6b1a`](https://github.com/cla-bit/PayStackEase/commit/87f6b1afc1d93d3d42ae19e0245ed75dc46a59ce))

* included datetime in the convert_to_string method ([`8f31b88`](https://github.com/cla-bit/PayStackEase/commit/8f31b8818468bd38647ba8fa614dd72c95883187))

* updated test file: conftest ([`718bae4`](https://github.com/cla-bit/PayStackEase/commit/718bae4d5af7653079729a31c6dd5f3767f8c83a))

* added and updated async and sync test files: verification ([`6083e8f`](https://github.com/cla-bit/PayStackEase/commit/6083e8f7af2996d9ebaf0b1bb0875128dc5250b5))

* added and updated async and sync test files: transfers_control ([`ae0fb79`](https://github.com/cla-bit/PayStackEase/commit/ae0fb79b2795207f3266bef94518f3f4c1b57999))

* added and updated async and sync test files: transfers ([`f6b9966`](https://github.com/cla-bit/PayStackEase/commit/f6b996604c88ea4ea4da8fdfc2581cb14db77537))

* added and updated async and sync test files: transfer_recipients ([`dec0fdc`](https://github.com/cla-bit/PayStackEase/commit/dec0fdc77f34f5300d5e5d093bec91d59ff617ec))

* added and updated async and sync test files: transactions ([`2622e2c`](https://github.com/cla-bit/PayStackEase/commit/2622e2c51125dbd66093de7973207a7e2976d22f))

* added and updated async and sync test files: transaction splits ([`0e4fd5a`](https://github.com/cla-bit/PayStackEase/commit/0e4fd5ab15be313c03da9a9206b26ff389623a9f))

* added and updated async and sync test files: terminal ([`42631c7`](https://github.com/cla-bit/PayStackEase/commit/42631c7d5783843f7b3db02f2cf6de5cd52b1870))

* added and updated async and sync test files: subscriptions ([`d63b3cf`](https://github.com/cla-bit/PayStackEase/commit/d63b3cff27db1a700a78d7ab0641669ffec10115))

* added and updated async and sync test files: subaccounts ([`0604db1`](https://github.com/cla-bit/PayStackEase/commit/0604db19913e75a0a9896b51bf728329bfd0e9d2))

* added and updated async and sync test files: settlement ([`3f5cab4`](https://github.com/cla-bit/PayStackEase/commit/3f5cab4824abf21fe6f907a723e3ebd22d70196c))

* added and updated async and sync test files: refund ([`b77f195`](https://github.com/cla-bit/PayStackEase/commit/b77f1952846229df20b171bd312a4a390c371c7e))

* added and updated async and sync test files: products ([`ff7fef5`](https://github.com/cla-bit/PayStackEase/commit/ff7fef59012e9523f00a83c57fdb5006de04af2f))

* added and updated async and sync test files: plans ([`266c1ef`](https://github.com/cla-bit/PayStackEase/commit/266c1efcbeab0e2c29dca93bae7537023c48dbd7))

* added and updated async and sync test files: payment_request ([`a2c3e47`](https://github.com/cla-bit/PayStackEase/commit/a2c3e4723c90e3bf5abc4cc30dc2d3a411261aff))

* added and updated async and sync test files: payment_pages ([`f0336c6`](https://github.com/cla-bit/PayStackEase/commit/f0336c6719203d76d3fdfb9ec1aa6216458325d0))

* added and updated async and sync test files: miscellaneous ([`3710088`](https://github.com/cla-bit/PayStackEase/commit/371008887ea4bc0fb80db39440870104195d259a))

* added and updated async and sync test files: integration ([`e00a784`](https://github.com/cla-bit/PayStackEase/commit/e00a784367ce0572680c72e084efffba049a6186))

* added and updated async and sync test files: disputes ([`59c4b25`](https://github.com/cla-bit/PayStackEase/commit/59c4b25ba2abe71603a3513d8021ad113d25fb42))

* added and updated async and sync test files: dedicated_va ([`fa0e186`](https://github.com/cla-bit/PayStackEase/commit/fa0e186849cb62e241524344c1a975d2b6cd5632))

* added and updated async and sync test files: dva ([`d2954e0`](https://github.com/cla-bit/PayStackEase/commit/d2954e0fdc40a2bb38fdb026983718336bc6d10f))

* added a default value to the active in list_dedicated_virtual_account method ([`74909aa`](https://github.com/cla-bit/PayStackEase/commit/74909aa0cc0b204e446b852853fba8fd9f469fd8))

* updated and added test for async and sync apple pay, bulk charges and customers ([`9a16e58`](https://github.com/cla-bit/PayStackEase/commit/9a16e5826707ed54cd006e4789b38d0bc82ef9e9))

* updated and added test for async and sync charges. ([`a5acd7c`](https://github.com/cla-bit/PayStackEase/commit/a5acd7cd2b648128db31cdefa00b334a7ba68e5a))

* added test for bulk charges and updated conftest and test_aapple_pay. ([`943693b`](https://github.com/cla-bit/PayStackEase/commit/943693bc0bce89544ec58f1d2ca15aded0d72f23))

* updated test base charges script files ([`c8dd403`](https://github.com/cla-bit/PayStackEase/commit/c8dd40331a50aa28512757432d0e617e0048e311))

* added test scrip files ([`6c518b7`](https://github.com/cla-bit/PayStackEase/commit/6c518b76b48c275cc2463a45c6ee2db13c4a692c))

* updated the following py scripts: conftest and test_aapple_pay ([`89f7bc1`](https://github.com/cla-bit/PayStackEase/commit/89f7bc1d346b3c4656b834c998b22de534e00617))

* updated the following py scripts:  base and abase ([`7182a15`](https://github.com/cla-bit/PayStackEase/commit/7182a15df331173b65451cb047020174f948de9b))

* updated the following py scripts:  conftest, test_aapple_pay ([`1e3fb55`](https://github.com/cla-bit/PayStackEase/commit/1e3fb5515a0af234e846e5d43bcf0b9f62202982))

* updated the following py scripts:  conftest, test_abase, abase and base ([`8e6f916`](https://github.com/cla-bit/PayStackEase/commit/8e6f9165a8e40e7252d7c045d62678ec95ee0db0))

* updated the following py scripts:  conftest and test_abase ([`f3cfafa`](https://github.com/cla-bit/PayStackEase/commit/f3cfafae02975e6eec960e3df41cb46ed18ee72b))

* Update test_abase.py ([`9f04b11`](https://github.com/cla-bit/PayStackEase/commit/9f04b116ee0998d180d0d60694f2ff20cf2af54d))

* Update test_abase.py ([`7d0af21`](https://github.com/cla-bit/PayStackEase/commit/7d0af21d5bedf4902359b42c49da8fe03efc198b))

* updated gitignore ([`e79cb5b`](https://github.com/cla-bit/PayStackEase/commit/e79cb5b138ee32a032373e73f03d42188a315f0a))

* updated test files: abase ([`286b7ad`](https://github.com/cla-bit/PayStackEase/commit/286b7ad29bafd2165f5d2b1b79c543ae16589f86))

* updated test files: abase ([`c3ed3f0`](https://github.com/cla-bit/PayStackEase/commit/c3ed3f02c641747e83386b9e6ebad5802045a4f0))

* updated test files: abase and conftest ([`f468a00`](https://github.com/cla-bit/PayStackEase/commit/f468a006f8a9e0b2c111a24863e7e48d5105e65e))

* updated files ([`1586210`](https://github.com/cla-bit/PayStackEase/commit/158621065b6d1cd47daa08a3e66eac785c67f234))

* updated test files: abase and base ([`b535e21`](https://github.com/cla-bit/PayStackEase/commit/b535e2175ed5ecb3a4e4b28a79a68d0f395e143f))

* updated files ([`ca93949`](https://github.com/cla-bit/PayStackEase/commit/ca93949b100c5815d21b84460fe99d6ecb9865d2))

* updated files ([`3421ce3`](https://github.com/cla-bit/PayStackEase/commit/3421ce3a591b85f7c39a7580a547f99d83087145))

* updated test_base script files ([`50adaae`](https://github.com/cla-bit/PayStackEase/commit/50adaae30ef9b2a310513900d4490881e1633b6e))

* added test script files ([`fbee318`](https://github.com/cla-bit/PayStackEase/commit/fbee3186c85f154d7e0fcfe45625a29d5bf2ac63))

* updated gitignore file ([`9d14ed2`](https://github.com/cla-bit/PayStackEase/commit/9d14ed27fbc6b82157c3277d6cf2409842f887bb))

* updated requirements file ([`d5e623e`](https://github.com/cla-bit/PayStackEase/commit/d5e623e17929a71b58a58554b2699f008e8f63c5))

* updated usage rst file ([`bf817d4`](https://github.com/cla-bit/PayStackEase/commit/bf817d463b4bad236f9be2d545233a21ed1a9482))

* updated usage rst file ([`12af2a0`](https://github.com/cla-bit/PayStackEase/commit/12af2a022e05726cc9c0ee58ea381af3a4881f1a))

* updated usage rst file ([`a51d5bd`](https://github.com/cla-bit/PayStackEase/commit/a51d5bd8682b0a9d0b2de47da07b86cb2bc8bb06))

* Update usage.rst ([`0e3d7d2`](https://github.com/cla-bit/PayStackEase/commit/0e3d7d2bb74d027aece2200b9ed8ec6d6253200d))

* Update usage.rst ([`421ad96`](https://github.com/cla-bit/PayStackEase/commit/421ad961870ab41c3b82128acf1b217391e5cc71))

* Update index.rst ([`51e0839`](https://github.com/cla-bit/PayStackEase/commit/51e0839d101977955425cd60762c1f6281e5dc94))

* Update usage.rst ([`10b1643`](https://github.com/cla-bit/PayStackEase/commit/10b164341e0c1d8bdba53797ea33a60ac8697f64))

* Update submodules.rst ([`97b2444`](https://github.com/cla-bit/PayStackEase/commit/97b2444376a129bf3adc70df5f0178b88515be7b))

* Update paystackease.helpers.rst ([`8c30bbb`](https://github.com/cla-bit/PayStackEase/commit/8c30bbb1b299525ba6fc4dc817610cd270d26ade))

* Update paystackease.async_apis.rst ([`34e2181`](https://github.com/cla-bit/PayStackEase/commit/34e21811daf12b74145eb5d68b44947a192229c2))

* Update paystackease.apis.rst ([`8b4fecb`](https://github.com/cla-bit/PayStackEase/commit/8b4fecb953df26e14eb9f6ad81c2b3d7ac1bedd0))

* Update index.rst ([`27f136f`](https://github.com/cla-bit/PayStackEase/commit/27f136fa6f7a355590f59fc5a5b51cb0b75908a5))

* Update index.rst ([`6e06140`](https://github.com/cla-bit/PayStackEase/commit/6e061407c06919878e236fe670e04dc6f867796b))

* Update index.rst ([`ee9e74e`](https://github.com/cla-bit/PayStackEase/commit/ee9e74ee40612132e948c620ee97846f31987fbb))

* Update index.rst ([`c376954`](https://github.com/cla-bit/PayStackEase/commit/c376954a069dc7436ed3ab0f0a52ab26af4e4a65))

* updated index rst file ([`56e3fb2`](https://github.com/cla-bit/PayStackEase/commit/56e3fb2b9f572fb180f3537059f8be5175ea9062))

* updated index rst file ([`3f915f7`](https://github.com/cla-bit/PayStackEase/commit/3f915f7fbc4d17656a68f431f731f70e3a274191))

* updated index rst file ([`fd8732b`](https://github.com/cla-bit/PayStackEase/commit/fd8732bc92215c880b2df690621a96e10472f2b0))

* updated rst file ([`441c4fe`](https://github.com/cla-bit/PayStackEase/commit/441c4feb2ea9309245b80ce40a43deb4fbbc7a99))

* updated rst file ([`c717506`](https://github.com/cla-bit/PayStackEase/commit/c717506aed4402ca9a53141c4bdd647a855b9b59))

* updated index rst file ([`a9bba20`](https://github.com/cla-bit/PayStackEase/commit/a9bba20b553bc475051da3a45cfe37a8d3f10a04))

* added and updated rst files ([`1dcd685`](https://github.com/cla-bit/PayStackEase/commit/1dcd685dab304a01deb6abf9b058c1cf08e31336))

* Update averification.py ([`db45e0c`](https://github.com/cla-bit/PayStackEase/commit/db45e0c52861d9a42f086a5ec6eb34ac7c34b7a7))

* Update atransfers_control.py ([`ca06a21`](https://github.com/cla-bit/PayStackEase/commit/ca06a21d92524bb864f49df6b1e7f94181f38d68))

* Update atransfers.py ([`b04bfb0`](https://github.com/cla-bit/PayStackEase/commit/b04bfb0b2fe3f0ff8f6751a1244ebb980ca1604d))

* Update atransfer_recipients.py ([`2939318`](https://github.com/cla-bit/PayStackEase/commit/29393187473aaba80f49157fca1767847e4e0653))

* Update atransactions.py ([`63fb04e`](https://github.com/cla-bit/PayStackEase/commit/63fb04eb71d3bbb75635e40acff69ac582516e4d))

* Update atransaction_splits.py ([`2495fe9`](https://github.com/cla-bit/PayStackEase/commit/2495fe9f4ccbbabce2e3b67879ac91616a00b5b3))

* Update aterminal.py ([`718a51a`](https://github.com/cla-bit/PayStackEase/commit/718a51ae4b0f3f29963a5268f1b75a3bfde0682c))

* Update asubscriptions.py ([`84f9ed0`](https://github.com/cla-bit/PayStackEase/commit/84f9ed092a6b421cb26ebd4f5d073fe7bf286995))

* Update asubaccounts.py ([`904fb1b`](https://github.com/cla-bit/PayStackEase/commit/904fb1b7551d543fc3390899d1074d56e128b018))

* Update asettlements.py ([`c397307`](https://github.com/cla-bit/PayStackEase/commit/c3973072b75847be5da39fdaca520381dd41eccd))

* Update arefund.py ([`0fbd587`](https://github.com/cla-bit/PayStackEase/commit/0fbd587da46a61754961f713be388bb888529f38))

* Update aproducts.py ([`94e5991`](https://github.com/cla-bit/PayStackEase/commit/94e5991509376b6cfad4055570085832f8ec993c))

* Update aplans.py ([`c611619`](https://github.com/cla-bit/PayStackEase/commit/c611619c8824910ce4c8738cb63ef90aed4250f2))

* Update apayment_requests.py ([`9489776`](https://github.com/cla-bit/PayStackEase/commit/9489776258d32be395063d3be4b465fee149ef36))

* Update apayment_pages.py ([`8984a7a`](https://github.com/cla-bit/PayStackEase/commit/8984a7ae8401f92978923a4afc446d6ca7859832))

* Update amiscellaneous.py ([`0d6581d`](https://github.com/cla-bit/PayStackEase/commit/0d6581deea18ea7241c222e2ce60531e59433e2e))

* Update aintegration.py ([`c1ec78c`](https://github.com/cla-bit/PayStackEase/commit/c1ec78c2e545bfe89db597361c5d456dac90d3e1))

* Update adisputes.py ([`86d5ec0`](https://github.com/cla-bit/PayStackEase/commit/86d5ec0d0eaa8b8554b3a271f5b0e75cc3eade03))

* Update adedicated_virtual_accounts.py ([`aa1b57d`](https://github.com/cla-bit/PayStackEase/commit/aa1b57db7e52ad1a22644c632e50f528badff15e))

* Update acustomers.py ([`a9a815f`](https://github.com/cla-bit/PayStackEase/commit/a9a815f9c1ff003c9ec5265480390380c92ec5ef))

* Update acharges.py ([`5dc1e72`](https://github.com/cla-bit/PayStackEase/commit/5dc1e72959e55b82d45192143d4f290bd60b0cc7))

* Update abulk_charges.py ([`17a3f09`](https://github.com/cla-bit/PayStackEase/commit/17a3f09593b1519e7fdc6e57ff5bc8b0bc02f191))

* Update aapple_pay.py ([`8c93779`](https://github.com/cla-bit/PayStackEase/commit/8c93779d22065fe7a93240e4c36ae4d287733db4))

* Update verification.py ([`9085fd8`](https://github.com/cla-bit/PayStackEase/commit/9085fd853fc0d0abbb28aeac7b94142a8bdc6214))

* Update transfers_control.py ([`1f3b218`](https://github.com/cla-bit/PayStackEase/commit/1f3b218e3b9594e7dec9d1d69701dd12714445b5))

* Update transfers.py ([`cefbffc`](https://github.com/cla-bit/PayStackEase/commit/cefbffcd1f7eb1311974d8e02c811fe8dfaa0690))

* Update transfer_recipients.py ([`eb60a82`](https://github.com/cla-bit/PayStackEase/commit/eb60a823f2fad510b58b342bf8dc57837e83c6cd))

* Update transactions.py ([`bde5f91`](https://github.com/cla-bit/PayStackEase/commit/bde5f91a4f771ca91429ef75c5cc9797b0b7000c))

* Update transaction_splits.py ([`0ba87a0`](https://github.com/cla-bit/PayStackEase/commit/0ba87a0ff15b8636b7f65b5f164c2b44e1817fe2))

* Update terminal.py ([`3223dc4`](https://github.com/cla-bit/PayStackEase/commit/3223dc41cf9f102f1ae27620293f0e7d8214065f))

* Update subscriptions.py ([`3c2a40c`](https://github.com/cla-bit/PayStackEase/commit/3c2a40cfe7e3f3d577db92dbc590878d5d7daa5a))

* Update subaccounts.py ([`3fc1b06`](https://github.com/cla-bit/PayStackEase/commit/3fc1b063247aa8bff2eee1520d55eeaaf6ee97d7))

* Update settlements.py ([`310b326`](https://github.com/cla-bit/PayStackEase/commit/310b326767b3a452a6f56a2cc0c8da9135603c96))

* Update refund.py ([`8055dcd`](https://github.com/cla-bit/PayStackEase/commit/8055dcd95e2c358166fc5f38d947a399e3a1bb1c))

* Update products.py ([`43eaaef`](https://github.com/cla-bit/PayStackEase/commit/43eaaef143cf1fc1334acb9a252c267289cb23a6))

* Update plans.py ([`3195450`](https://github.com/cla-bit/PayStackEase/commit/3195450dc229e63383f2a40adb91477eb3de441e))

* Update payment_requests.py ([`f4cd596`](https://github.com/cla-bit/PayStackEase/commit/f4cd59613dbb882da4b8781d3c736de3013246d7))

* Update payment_pages.py ([`b777499`](https://github.com/cla-bit/PayStackEase/commit/b777499dec67ae4584e4468be6fa550547c37d9e))

* Update miscellaneous.py ([`e8a7d2e`](https://github.com/cla-bit/PayStackEase/commit/e8a7d2eaaf8381564b7c8ef196c95a4b03d24b11))

* Update integration.py ([`27d9df8`](https://github.com/cla-bit/PayStackEase/commit/27d9df87dbed86c57bed9050be91523c0253c4e3))

* Update disputes.py ([`7038eaf`](https://github.com/cla-bit/PayStackEase/commit/7038eaffdd99eb712f1b04470748b31f3a36ab91))

* Update dedicated_virtual_accounts.py ([`cfb2ef0`](https://github.com/cla-bit/PayStackEase/commit/cfb2ef03332b31da5707d3598f901e060f77efe2))

* Update customers.py ([`33f82b0`](https://github.com/cla-bit/PayStackEase/commit/33f82b0ea6d98e2f180275f2cef54c7ca06424c2))

* Update charges.py ([`628c57f`](https://github.com/cla-bit/PayStackEase/commit/628c57ff058335234f3966de71ba1593f6199f12))

* Update bulk_charges.py ([`511ee7f`](https://github.com/cla-bit/PayStackEase/commit/511ee7fe451f6ccfc2196ae37690732c013683cb))

* Update apple_pay.py ([`d9b0c61`](https://github.com/cla-bit/PayStackEase/commit/d9b0c61c4595ab3b3955962d0435496849796b8a))

* deleted and updated files ([`132f4b7`](https://github.com/cla-bit/PayStackEase/commit/132f4b721b782d32c496cff0ee94af5bb171e230))

* added rst files and updated conf.py and index.rst ([`6074d62`](https://github.com/cla-bit/PayStackEase/commit/6074d621ca6bbc1c32482771fe471408106407b2))

* updated apis and async_apis init files ([`6ecaf9e`](https://github.com/cla-bit/PayStackEase/commit/6ecaf9e0fc0ad7fd817c0cb2fea95b9f40bad30e))

* removed rst files ([`b13fdf2`](https://github.com/cla-bit/PayStackEase/commit/b13fdf237ab86dbd9bd95391a07bb8ec0b8f5d7d))

* updated modules and packages ([`a999827`](https://github.com/cla-bit/PayStackEase/commit/a999827a71595b0f7ef01f7c32f6be2f759048cb))

* updated index.rst file ([`52ba7b0`](https://github.com/cla-bit/PayStackEase/commit/52ba7b000fb3b1cf107d60c8d19cd3e51073a4b9))

* updated rst files ([`41628cf`](https://github.com/cla-bit/PayStackEase/commit/41628cf281ec7d64599095e67fab86b1c0e562ba))

* updated rst files ([`725f55f`](https://github.com/cla-bit/PayStackEase/commit/725f55f6f0cae16809a8323eac59fc176e512ea0))

* updated rst files ([`da9a824`](https://github.com/cla-bit/PayStackEase/commit/da9a824524e9515f3a54d79d16ce9b0e3f1109cf))

* updated rst files ([`132c40d`](https://github.com/cla-bit/PayStackEase/commit/132c40d22990127f50361d643804da661daebac6))

* updated the following rst files: paysatckease.apis and paystackease.async_apis ([`c0a1390`](https://github.com/cla-bit/PayStackEase/commit/c0a1390175cd0fda406169ece75974721159de9c))

* updated the following rst files: index, submodules, abase, base, paystack, apaystack ([`4c3fa9c`](https://github.com/cla-bit/PayStackEase/commit/4c3fa9cbed69c79e1c104bdc112715f7752d5553))

* updated rst files ([`85d2176`](https://github.com/cla-bit/PayStackEase/commit/85d217669c5befc08e735d57b8392b31942d3345))

* updated rst files ([`1bedf61`](https://github.com/cla-bit/PayStackEase/commit/1bedf61fab712b64d25f7a821acac63b1c38ac02))

* updated rst files ([`d82f06b`](https://github.com/cla-bit/PayStackEase/commit/d82f06b4c8f3152b394eb50900bad036d0b54bf9))

* updated rst files ([`1f629bc`](https://github.com/cla-bit/PayStackEase/commit/1f629bcb983a41a1a31abe67ec2c358648794f21))

* updated rst files ([`d514583`](https://github.com/cla-bit/PayStackEase/commit/d5145838afad323a3c9650f6a0efb591d5c4a03d))

* updated rst files ([`2e0f3f2`](https://github.com/cla-bit/PayStackEase/commit/2e0f3f2ee5e64e72154a60175bcdd7b481ad21fe))

* updated rst files ([`a73ac9b`](https://github.com/cla-bit/PayStackEase/commit/a73ac9bbbf11e6e8f4b1b0f88360554d5eeb4517))

* updated rst files ([`3b316d6`](https://github.com/cla-bit/PayStackEase/commit/3b316d6162f139ad2975d6fa8b8e58fa83b1ef22))

* updated rst files ([`456e985`](https://github.com/cla-bit/PayStackEase/commit/456e9858f64e96289d20eb3bf59324dea28e97e8))

* updated rst files ([`04cab17`](https://github.com/cla-bit/PayStackEase/commit/04cab178d363d7678cb0c1260f516bc8c3020910))

* updated charges, customers, acharges, acustomers, paystack.apis, and paystack.async_apis rst files ([`c1657e7`](https://github.com/cla-bit/PayStackEase/commit/c1657e7ebc3c54b32e47b7185bad59627135b114))

* updated files ([`1d1f368`](https://github.com/cla-bit/PayStackEase/commit/1d1f3689e2d35556adf759c8d32e73f9a7c91130))

* updated pyproject file ([`571398e`](https://github.com/cla-bit/PayStackEase/commit/571398e6aad4a53232df84713574c233179ef1a8))

* updated ([`d8dd9d5`](https://github.com/cla-bit/PayStackEase/commit/d8dd9d54ab780a335dd64d25e6369ffb23e3099c))

* updated ([`8092cab`](https://github.com/cla-bit/PayStackEase/commit/8092cab96284ab37b9a87ee072b63153665e9d96))

* updated ([`ec6ea88`](https://github.com/cla-bit/PayStackEase/commit/ec6ea8875d0fc1b4ecba76afefed011377b465eb))

* updated ([`56973fb`](https://github.com/cla-bit/PayStackEase/commit/56973fb463aa67c0b4cdbdffb78e7a918672b8a5))

* updated gitignore file ([`ca95927`](https://github.com/cla-bit/PayStackEase/commit/ca95927cc540765d2942560eb5493f55a6acdc6b))

* Merge remote-tracking branch &#39;origin/master&#39; ([`6df1e3d`](https://github.com/cla-bit/PayStackEase/commit/6df1e3d4798fc04d94e2e7297f94cc6a44114d44))

* Delete .idea directory ([`5c7ddd0`](https://github.com/cla-bit/PayStackEase/commit/5c7ddd09df8cea18fd9ef14697f9208d8a555c3e))

* updated gitignore file ([`6cc027c`](https://github.com/cla-bit/PayStackEase/commit/6cc027c0fa5a26a05df3082652a0ae87b82ec960))

* updated gitignore file ([`a56e655`](https://github.com/cla-bit/PayStackEase/commit/a56e655a055582b67ba4315acca2099dbe1ae57b))

* Delete .idea directory ([`3c1e86f`](https://github.com/cla-bit/PayStackEase/commit/3c1e86f3d38e2e6bb99658ae836424c8eca6a57f))

* updated async and sync rst files: aapple, apple, abulkcharges, bulkcharges, paystackease.apis, and paystackease.async_apis. ([`3e57481`](https://github.com/cla-bit/PayStackEase/commit/3e574819c8d67329642b42a436ccfdb34ac41c8c))

* updated async and sync rst files: rst files ([`2be070f`](https://github.com/cla-bit/PayStackEase/commit/2be070f1803597a3694ac4f75d95343ede77dd64))

* updated async and sync rst files: bulkcharges and, abulkcharges. ([`a321631`](https://github.com/cla-bit/PayStackEase/commit/a321631ddfdd16dd9512a3dce0ecdf92d44fd024))

* updated async and sync rst files: applepay, aapplepay, bulkcharges, abulkcharges, paystackease.apis and paystackease.async_apis. ([`d2f78b1`](https://github.com/cla-bit/PayStackEase/commit/d2f78b10da3a0b4f0a8103ccf3e5830ffd38071f))

* updated async and sync rst files: applepay, aapplepay, paystackease.apis and paystackease.async_apis ([`8be279c`](https://github.com/cla-bit/PayStackEase/commit/8be279cf6fda0d7ac060c6a18dfb2d5dfef709a2))

* updated rst file ([`26da4f3`](https://github.com/cla-bit/PayStackEase/commit/26da4f3ba3ece036c960197b83316647e92cffaa))

* updated rst file ([`5169c77`](https://github.com/cla-bit/PayStackEase/commit/5169c77477560c2aa86e540b84a96feaaf33e574))

* updated apple pay rst file ([`4f49cf1`](https://github.com/cla-bit/PayStackEase/commit/4f49cf16767615e2e16342ced8f0d27337bf50a4))

* updated apple pay rst file ([`c0c3abc`](https://github.com/cla-bit/PayStackEase/commit/c0c3abc62fc1356ff5dc65a446df1a0c47a37815))

* updated rst file ([`026cb58`](https://github.com/cla-bit/PayStackEase/commit/026cb5864cda65597c60e433817303c78f91217d))

* updated abase, base, apaystack and paystack rst file ([`b216189`](https://github.com/cla-bit/PayStackEase/commit/b216189900192ff31e89d27968f509297dcfed36))

* updated abase.rst file ([`447ac33`](https://github.com/cla-bit/PayStackEase/commit/447ac3330ad050aca6d08e028f7df08a25023e08))

* updated rst files ([`7f4735c`](https://github.com/cla-bit/PayStackEase/commit/7f4735c542347940a26acc7c353634e5e80792f7))

* updated rst files ([`491e7bd`](https://github.com/cla-bit/PayStackEase/commit/491e7bda3ea35ad72fa140ffa353843ab1e2161a))

* updated rst files ([`c208a50`](https://github.com/cla-bit/PayStackEase/commit/c208a505cb10d8382acfb268bcbece6b588d64be))

* updated conf file ([`b97a94f`](https://github.com/cla-bit/PayStackEase/commit/b97a94f42cf7949d9d09d313c51dc3aaf67da164))

* Update pyproject.toml ([`cc63209`](https://github.com/cla-bit/PayStackEase/commit/cc6320950231e052191f716c16ac25e6fefbf058))

* Update .readthedocs.yaml ([`b26ab77`](https://github.com/cla-bit/PayStackEase/commit/b26ab77a32fb26b2b9825d373c24ca4aad082ade))

* Update .readthedocs.yaml ([`6fa0fc2`](https://github.com/cla-bit/PayStackEase/commit/6fa0fc29a14127c914e5879fc76085cd959db7c0))

* updated reaadthedocs file ([`2247df6`](https://github.com/cla-bit/PayStackEase/commit/2247df61f801c4e1ee2fb4782f888f57b8cd786c))

* updated reaadthedocs file ([`fdd6c4c`](https://github.com/cla-bit/PayStackEase/commit/fdd6c4cae65559ac4c312cf4abb26115f3c70822))

* updated reaadthedocs file ([`42bb44a`](https://github.com/cla-bit/PayStackEase/commit/42bb44ab161c6756e027f357a2ef4ce59d20c710))

* updated reaadthedocs file ([`c809214`](https://github.com/cla-bit/PayStackEase/commit/c8092142ae47a80108079d8997e63b211e8dc4ba))

* updated requirements file ([`fd20cf8`](https://github.com/cla-bit/PayStackEase/commit/fd20cf8ea4929f02ea9ba1c1ce9b2970077436af))

* added .readthedocs.yaml file ([`b75b328`](https://github.com/cla-bit/PayStackEase/commit/b75b32822ea7fb19fe102441177b79008eb4ebb7))

* removed .readthedocs.yaml file ([`badb3fb`](https://github.com/cla-bit/PayStackEase/commit/badb3fb55adc7a36142266078bbbb29b24deb2c4))

* updated documentation ([`da95bec`](https://github.com/cla-bit/PayStackEase/commit/da95bec6124113272e375e50b7bd0efa88eeb33d))

* updated documentation ([`40ebc62`](https://github.com/cla-bit/PayStackEase/commit/40ebc6266d7a76f1fab71fee78aec6f85f4893c8))

* updated documentation ([`76f0449`](https://github.com/cla-bit/PayStackEase/commit/76f04490a4b338bb3070ed055243e96b0e82d47c))

* updated gitignore ([`cf34ba3`](https://github.com/cla-bit/PayStackEase/commit/cf34ba3b9b8b3c446323339d2e449b9651a08897))

* added documentations ([`4373daf`](https://github.com/cla-bit/PayStackEase/commit/4373daf31f5c91b6e0264deb63dafc559a04638f))

* added documentations ([`e37b182`](https://github.com/cla-bit/PayStackEase/commit/e37b182a8ba92c2f0504fe486d5398b3947e5d63))

* added documentations ([`15b3d13`](https://github.com/cla-bit/PayStackEase/commit/15b3d1368908cd7657cfcaa297627055734641cc))

* added documentations ([`1da0939`](https://github.com/cla-bit/PayStackEase/commit/1da0939be4046b68e5a2956e464a2c437e245969))

* added documentations ([`f9ce655`](https://github.com/cla-bit/PayStackEase/commit/f9ce655484f41b394824c53272d50705594b5229))

* added documentations ([`9edd31d`](https://github.com/cla-bit/PayStackEase/commit/9edd31dc26116c247daf1fcfe15f1329e9089a5d))

* added documentations ([`38ea001`](https://github.com/cla-bit/PayStackEase/commit/38ea0012c93edb4980eaf7692d685139c872f66e))

* updated helpers ([`27e96b6`](https://github.com/cla-bit/PayStackEase/commit/27e96b65113e96841f823080809b0555d8f5afd7))

* updated docstrings ([`3c73b01`](https://github.com/cla-bit/PayStackEase/commit/3c73b01b489f488e804d68ee8a6feac97e1abdc2))

* updated docstrings ([`b139c3b`](https://github.com/cla-bit/PayStackEase/commit/b139c3b3c429e6682a293268382d2b81404cf7e8))

* updated sync and async files: transfer control and verification ([`eaef2d8`](https://github.com/cla-bit/PayStackEase/commit/eaef2d89f312ecf76dfe75ab7880bf0629496440))

* updated sync and async files: transfer ([`cab2887`](https://github.com/cla-bit/PayStackEase/commit/cab2887c10cec20164310152506d3d506a2c0392))

* updated sync and async files: transfer_recipients ([`cf16a7c`](https://github.com/cla-bit/PayStackEase/commit/cf16a7c9ff70f249647a82cda1fee50b75b84618))

* updated sync and async files: transaction ([`3417f53`](https://github.com/cla-bit/PayStackEase/commit/3417f5383d94b7cb14a1a07dd0ac581b401ee914))

* updated sync and async files: transaction_splits ([`c7887d5`](https://github.com/cla-bit/PayStackEase/commit/c7887d5931a33bd4bc2bbdc8b611cbf9d0776e70))

* updated sync and async files: terminal ([`47c8815`](https://github.com/cla-bit/PayStackEase/commit/47c8815c998935e3bd3a9e8eaea2e87f21cf760e))

* updated sync and async files: refund, settlement, subaccount and subscription ([`b48180c`](https://github.com/cla-bit/PayStackEase/commit/b48180c225971df883f77c3db3582ff52995fb25))

* updated sync and async files: payment request, payment pages, plans and products ([`0d93943`](https://github.com/cla-bit/PayStackEase/commit/0d9394386a5fa4e945c90b884b60c971951e6ca1))

* updated sync and async files: disputes, integration and miscellaneous ([`b6b3880`](https://github.com/cla-bit/PayStackEase/commit/b6b3880bcd0d4618dddc834bccbb1fb217a5d430))

* updated sync and async files: dedicated virtual account ([`f9b793b`](https://github.com/cla-bit/PayStackEase/commit/f9b793b2abdb1c8452d8115ff856733d39212723))

* updated sync and async files: apple pay, bulk charges, charges, and others ([`c6a69e4`](https://github.com/cla-bit/PayStackEase/commit/c6a69e436ef1f7a75802d66cd4eba921b0e5c770))

* updated sync and async charges scripts ([`0b2b854`](https://github.com/cla-bit/PayStackEase/commit/0b2b8540ecb1618fc3b9f6f4a49b1f297a43788c))

* updated sync and async apple pay and bulk charges scripts ([`536bd02`](https://github.com/cla-bit/PayStackEase/commit/536bd02a7cbb584f751063e9f3e66698be736eec))

* updated project ([`8ccde81`](https://github.com/cla-bit/PayStackEase/commit/8ccde81a06e28b8cdb35872fba95c8f3eb1a92c3))

* updated project ([`45083d1`](https://github.com/cla-bit/PayStackEase/commit/45083d14f1894704bfc256c478e0cc14c2af2b69))

* updated project ([`c262f07`](https://github.com/cla-bit/PayStackEase/commit/c262f077402af57d55f18e5f3f8568152c23409c))

* updated pyproject.tomlt ([`4339a39`](https://github.com/cla-bit/PayStackEase/commit/4339a394c0418907e86b8059a1e10b527aad9eb6))

* updated CHANGELOG.md and CONTRIBUTING.md ([`1b7edac`](https://github.com/cla-bit/PayStackEase/commit/1b7edac86e782cb6a284f422fc7fd8d28464fb76))

* updated README.md and SECURITY.md ([`9e577c9`](https://github.com/cla-bit/PayStackEase/commit/9e577c9e9be9509fecf869bd1b5ae44f6234a62e))

* updated README.md ([`a4152b7`](https://github.com/cla-bit/PayStackEase/commit/a4152b793a6d677a6135db94db94d7da85c612e2))

* updated the base and abase script file and added error.py ([`d6c0686`](https://github.com/cla-bit/PayStackEase/commit/d6c068629e6b5481fbe4d3367946247647585047))

* added events and webhook script files ([`91568f8`](https://github.com/cla-bit/PayStackEase/commit/91568f866e3251f0695369045cb931e869e3fe34))

* Create poetry lock and pyproject.toml ([`f7b5eba`](https://github.com/cla-bit/PayStackEase/commit/f7b5eba9db69adf8d7f5b27962594306400d1995))

* Create SECURITY.md ([`1f4f7c5`](https://github.com/cla-bit/PayStackEase/commit/1f4f7c5f8363530b697d7b50136015e768981bb1))

* Added some files ([`4ee49bc`](https://github.com/cla-bit/PayStackEase/commit/4ee49bcf300509335a485308db116a1e3330ba3b))

* Delete api_docs directory ([`8f156b8`](https://github.com/cla-bit/PayStackEase/commit/8f156b8802b6965ad246c6cca681a20c83a5287f))

* added an image ([`568b116`](https://github.com/cla-bit/PayStackEase/commit/568b11678263171bb2c7bcbaec4ca5c69c212574))

* Create image.md

. ([`0193f4f`](https://github.com/cla-bit/PayStackEase/commit/0193f4f39cf70de6c43487ef30fe02794923d645))

* Create apple_pay.md

added apple_pay.md ([`70b0357`](https://github.com/cla-bit/PayStackEase/commit/70b0357cf72faf6b02c53a37eba1323c38d0ea38))

* updated the readme file ([`37a0260`](https://github.com/cla-bit/PayStackEase/commit/37a0260ae058a50e710dda9eeae58cca95efa73f))

* updated the base and abase script files. ([`9d1a447`](https://github.com/cla-bit/PayStackEase/commit/9d1a447e3650ae6e371f0f6213bc139c920a41ce))

* updated the base and abase script files. ([`5090c9a`](https://github.com/cla-bit/PayStackEase/commit/5090c9ad26e5e0bd58b89bdea436be3abf7fd860))

* updated the pyproject.toml, removed tests folder, added ReadMe.md and apple_pay.md files ([`7ab3966`](https://github.com/cla-bit/PayStackEase/commit/7ab39661e194688abff8c61feee1036bec9d8ce6))

* Made changes to pyproject.toml ([`36d164c`](https://github.com/cla-bit/PayStackEase/commit/36d164c9de12bf6efd11cb7f323599c147d98067))

* Made changes to pyproject.toml ([`4d726c1`](https://github.com/cla-bit/PayStackEase/commit/4d726c1f62068529157862d0c719bc4956916360))

* Made changes to pyproject.toml ([`59ab8eb`](https://github.com/cla-bit/PayStackEase/commit/59ab8eb54b04af07ac7fe7c2ff03b26bf93ecffa))

* Merge remote-tracking branch &#39;github/master&#39; ([`aeb98c4`](https://github.com/cla-bit/PayStackEase/commit/aeb98c40bc70e587fadacd36f8b0a626b0f03226))

* Merge remote-tracking branch &#39;github/master&#39; ([`a97e40a`](https://github.com/cla-bit/PayStackEase/commit/a97e40aff085d361ccf205873ba53d0c8ba34690))

* Merge remote-tracking branch &#39;github/master&#39; ([`22a46ca`](https://github.com/cla-bit/PayStackEase/commit/22a46caf2b6f541064e6506122f14622d6a36d78))

* Merge remote-tracking branch &#39;github/master&#39; ([`8ca206e`](https://github.com/cla-bit/PayStackEase/commit/8ca206e28476494542fdc10b682d112b339cbac1))

* Merge remote-tracking branch &#39;github/master&#39; ([`a326feb`](https://github.com/cla-bit/PayStackEase/commit/a326feb2887fdcf87bfbd1fe8e27110afbecd42c))

* Merge remote-tracking branch &#39;github/master&#39; ([`5261806`](https://github.com/cla-bit/PayStackEase/commit/52618066c6ad78f3c0154bb800b7657b417a307a))

* Merge remote-tracking branch &#39;github/master&#39; ([`45eb873`](https://github.com/cla-bit/PayStackEase/commit/45eb873249a8212dcaf4d7ac0a9f71726fa442d1))

* Removed the convert_to_string functino from _convert module. ([`0aa9b4c`](https://github.com/cla-bit/PayStackEase/commit/0aa9b4c23d4aef6d6bbfd8d25a243e158851f873))


## v0.1.0 (2024-03-04)

### Unknown

* Removed script files in pypoetry.toml ([`a096059`](https://github.com/cla-bit/PayStackEase/commit/a096059c38ecfcf706863c77e58bc04d88557056))

* Made changes to the pypoetry.toml file ([`17fed49`](https://github.com/cla-bit/PayStackEase/commit/17fed49501ca8f799b58e5bb9df81c33076c7de8))

* Initial Commit ([`c2e348d`](https://github.com/cla-bit/PayStackEase/commit/c2e348dfb5d9a33214ce03e1c992cd929ca4b5f8))
