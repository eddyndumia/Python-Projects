
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


words_dict = {"elephant": "a big animal",
              "dog": "a humans pet animal", "goat": "humans meat animal"}

print(words_dict["elephant"])


# adding keys and values

words_dict["cat"] = "a hunting animal with sharp ass claws"

print(words_dict)

# updating values

words_dict["cat"] = "an animal with claws and a tail"

print(words_dict["cat"])

# traversing a dictionary

# lets say we have a dictionary of words like a real dictionary, and we wanted to lookup the meaning of a certain keyword

myDict = {'name':'Edddy','school':'JKUAT', 'area':' '}

def googleDict(dict, search_term):
     if search_term in dict:
         return dict[search_term]
     return 'term does not exist'
    
print(googleDict(myDict, 'school'))


## traversing two

dict2 = {'a':'apple','b':'boy','c':'cat','d':'dog'}

def traverseDict (dict, value):
     #iterate this
     for keys in dict2:
          if dict2[keys] == value:
               return keys, value
     return 'no such value'

print(traverseDict(dict2, 'cat')) 