# coding: utf8

# Copyright 2017 Jacques Berger
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import hashlib
import sqlite3
import uuid

print "Nom d'utilisateur : "
username = raw_input()
print "Mot de passe : "
password = raw_input()

salt = uuid.uuid4().hex
hashed_password = hashlib.sha512(password + salt).hexdigest()

connection = sqlite3.connect('users.db')

connection.execute(("insert into users(utilisateur, salt, hash) "
                    "values(?, ?, ?)"), (username, salt, hashed_password))

connection.commit()
connection.close()
