from attr import attrs, attrib

@attrs
class Customer(object):

    customer_id = attrib(default=None)
    
    customer_name = attrib(default=None)
    customer_surname = attrib(default=None)
    customer_priority = attrib(default=None)
    customer_profile = attrib(default=None)

    registration_date = attrib(default=None)
    registration_method = attrib(default=None)
