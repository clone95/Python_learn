from attr import attrs, attrib

@attrs
class BasePortfolio(object):
    client_id = attrib(default=None)
        
@attrs
class ProductOne(BasePortfolio):
    product_id = attrib(default=88)
