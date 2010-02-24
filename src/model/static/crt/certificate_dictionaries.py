'''
Created on Feb 7, 2010

@author: frederikns
'''
from weakref import WeakValueDictionary

CATEGORIES = WeakValueDictionary()
CERTIFICATES = WeakValueDictionary()
CLASSES = WeakValueDictionary()
RECOMMENDATIONS = WeakValueDictionary()
RELATIONSHIPS = WeakValueDictionary()

def get_category(category_id):
    """Loads and returns the certificate category specified"""
    from model.static.crt.category import Category
    if category_id not in CATEGORIES:
        category = Category(category_id)
        CATEGORIES[category_id] = category
    return CATEGORIES[category_id]

def get_certificate(certificate_id):
    """Loads and returns the certificate certificate specified"""
    from model.static.crt.certificate import Certificate
    if certificate_id not in CERTIFICATES:
        certificate = Certificate(certificate_id)
        CERTIFICATES[certificate_id] = certificate
    return CERTIFICATES[certificate_id]

def get_certificate_class(certificate_class_id):
    """Loads and returns the certificate certificate_class specified"""
    from model.static.crt.certificate_class import CertificateClass
    if certificate_class_id not in CLASSES:
        certificate_class = CertificateClass(certificate_class_id)
        CLASSES[certificate_class_id] = certificate_class
    return CLASSES[certificate_class_id]

def get_recommendation(recommendation_id):
    """Loads and returns the certificate recommendation specified"""
    from model.static.crt.recommendation import Recommendation
    if recommendation_id not in RECOMMENDATIONS:
        recommendation = Recommendation(recommendation_id)
        RECOMMENDATIONS[recommendation_id] = recommendation
    return RECOMMENDATIONS[recommendation_id]

def get_relationship(relationship_id):
    """Loads and returns the certificate relationship specified"""
    from model.static.crt.relationship import Relationship
    if relationship_id not in RELATIONSHIPS:
        relationship = Relationship(relationship_id)
        RELATIONSHIPS[relationship_id] = relationship
    return RELATIONSHIPS[relationship_id]