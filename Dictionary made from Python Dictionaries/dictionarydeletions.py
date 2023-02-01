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


# deleting dictionaries

#pop method

myDict1 = {'animal':'cow','production':'milk','other production':'meat'}

# pop method deletes an item and returns the value of the key
key_for_item_to_be_deleted = 'animal'
deleted_item = myDict1.pop(key_for_item_to_be_deleted)

print('The dictionary is:', myDict1, 'and the deleted item is:', key_for_item_to_be_deleted,':',deleted_item)

#popitem

myDict2 = {'species':'fish','food':'floating carrots','blood type':'zeus'}

# popitem method deletes an arbitrary item and returns both the key and the value

deletedItem2 = myDict2.popitem()
print(deletedItem2)

# clear method

myDict3 = {'device':'mobile phone','keyboard type':'keypad','operating system':'android/ios'}

# clear method clears everything from the dictionary

myDict3.clear()

print(myDict3)



