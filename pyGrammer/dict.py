# -*- coding : utf-8 -*-
# @Author   :   stone
# @Github   :   https://github.com/stonedada
data={"name":"liu","klass":"two"}

def my_function(name,klass):
    my_name=name
    my_klass=klass
    print(my_name)
    print(my_klass)

my_function(**data)