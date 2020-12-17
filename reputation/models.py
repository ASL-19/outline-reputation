# Copyright 2020 ASL19 Organization
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

from abc import ABC


class ReputationSystemBase(ABC):
    """
    An abstract base class for reputation system

    A reputation system should at least provide two functions
    1. `server_level` to provide a server level based on user reputation
    2. `after_new_key` to adjust user's reputation after they requested a new user
    """

    @staticmethod
    def server_level(user_reputation: int) -> int:
        """
        This method returns a server level based on user's reputation

        :param user_reputation: User's reputation
        :return: Server level
        """
        return NotImplemented

    @staticmethod
    def after_new_key(curr_rep: int) -> int:
        """
        This method increases the user's reputation by 1 after each request

        :param curr_rep: current user's reputation
        :return: adjusted user's reputation
        """
        return NotImplemented
