
"""
 Copyright 2023 Eddy Ndumia

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at

      https://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
 """



words_dict = {"elephant":"a big animal","dog":"a humans pet animal","goat":"humans meat animal"}

print(words_dict["elephant"])


# adding keys and values

words_dict["cat"] = "a hunting animal with sharp ass claws"

print(words_dict)

# updating values

words_dict["cat"] = "an animal with claws and a tail"

print(words_dict["cat"])
