#    Copyright  2017 EasyStack, Inc
#    Authors: Hanxi Liu<apolloliuhx@gmail.com>
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

"""Exception definitions."""


class ZcpException(Exception):
    """The base exception class for all exceptions"""
    pass


class TemplateNotFound(ZcpException):
    """"Not find default template in zabbix"""
    pass


class NotImplementedError(NotImplementedError):
    """Not Implementation"""
    pass


class MappingFileNotFound(ZcpException):
    """Not find mapping.json"""
    pass


class LogConfigurationNotFound(ZcpException):
    """Error configuration about log file path"""
    pass
