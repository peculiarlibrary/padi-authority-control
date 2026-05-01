# Auto generated from padi_schema.yaml by pythongen.py version: 0.0.1
# Generation date: 2026-05-01T15:41:28
# Schema: PADI_Authority_Control
#
# id: https://github.com/peculiarlibrary/padi-authority-control
# description:
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import re
from dataclasses import dataclass
from datetime import (
    date,
    datetime,
    time
)
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Optional,
    Union
)

from jsonasobj2 import (
    JsonObj,
    as_dict
)
from linkml_runtime.linkml_model.meta import (
    EnumDefinition,
    PermissibleValue,
    PvFormulaOptions
)
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.formatutils import (
    camelcase,
    sfx,
    underscore
)
from linkml_runtime.utils.metamodelcore import (
    bnode,
    empty_dict,
    empty_list
)
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import (
    YAMLRoot,
    extended_float,
    extended_int,
    extended_str
)
from rdflib import (
    Namespace,
    URIRef
)

from linkml_runtime.linkml_model.types import String

metamodel_version = "1.7.0"
version = None

# Namespaces
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
PADI = CurieNamespace('padi', 'https://gitandu.com/padi/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
SKOS = CurieNamespace('skos', 'http://www.w3.org/2004/02/skos/core#')
DEFAULT_ = PADI


# Types

# Class references
class AuthorityRecordId(extended_str):
    pass


class BureauAgentId(extended_str):
    pass


class OutreachLogId(extended_str):
    pass


@dataclass(repr=False)
class AuthorityRecord(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SKOS["Concept"]
    class_class_curie: ClassVar[str] = "skos:Concept"
    class_name: ClassVar[str] = "AuthorityRecord"
    class_model_uri: ClassVar[URIRef] = PADI.AuthorityRecord

    id: Union[str, AuthorityRecordId] = None
    label: str = None
    depth_index: Union[str, "PadiDepth"] = None
    source: Optional[str] = None
    status: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AuthorityRecordId):
            self.id = AuthorityRecordId(self.id)

        if self._is_empty(self.label):
            self.MissingRequiredField("label")
        if not isinstance(self.label, str):
            self.label = str(self.label)

        if self._is_empty(self.depth_index):
            self.MissingRequiredField("depth_index")
        if not isinstance(self.depth_index, PadiDepth):
            self.depth_index = PadiDepth(self.depth_index)

        if self.source is not None and not isinstance(self.source, str):
            self.source = str(self.source)

        if self.status is not None and not isinstance(self.status, str):
            self.status = str(self.status)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class BureauAgent(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA["SoftwareAgent"]
    class_class_curie: ClassVar[str] = "schema:SoftwareAgent"
    class_name: ClassVar[str] = "BureauAgent"
    class_model_uri: ClassVar[URIRef] = PADI.BureauAgent

    id: Union[str, BureauAgentId] = None
    name: str = None
    mandate: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BureauAgentId):
            self.id = BureauAgentId(self.id)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self.mandate is not None and not isinstance(self.mandate, str):
            self.mandate = str(self.mandate)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OutreachLog(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PADI["OutreachLog"]
    class_class_curie: ClassVar[str] = "padi:OutreachLog"
    class_name: ClassVar[str] = "OutreachLog"
    class_model_uri: ClassVar[URIRef] = PADI.OutreachLog

    id: Union[str, OutreachLogId] = None
    target_node: str = None
    timestamp: str = None
    padi_depth_cited: Optional[Union[str, "PadiDepth"]] = None
    outcome: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OutreachLogId):
            self.id = OutreachLogId(self.id)

        if self._is_empty(self.target_node):
            self.MissingRequiredField("target_node")
        if not isinstance(self.target_node, str):
            self.target_node = str(self.target_node)

        if self._is_empty(self.timestamp):
            self.MissingRequiredField("timestamp")
        if not isinstance(self.timestamp, str):
            self.timestamp = str(self.timestamp)

        if self.padi_depth_cited is not None and not isinstance(self.padi_depth_cited, PadiDepth):
            self.padi_depth_cited = PadiDepth(self.padi_depth_cited)

        if self.outcome is not None and not isinstance(self.outcome, str):
            self.outcome = str(self.outcome)

        super().__post_init__(**kwargs)


# Enumerations
class PadiDepth(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="PadiDepth",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "1",
            PermissibleValue(
                text="1",
                description="Surface Level"))
        setattr(cls, "2",
            PermissibleValue(
                text="2",
                description="Foundational"))
        setattr(cls, "3",
            PermissibleValue(
                text="3",
                description="Operational"))
        setattr(cls, "4",
            PermissibleValue(
                text="4",
                description="Advanced"))
        setattr(cls, "5",
            PermissibleValue(
                text="5",
                description="Sovereign"))

# Slots
class slots:
    pass

slots.authorityRecord__id = Slot(uri=PADI.id, name="authorityRecord__id", curie=PADI.curie('id'),
                   model_uri=PADI.authorityRecord__id, domain=None, range=URIRef)

slots.authorityRecord__label = Slot(uri=PADI.label, name="authorityRecord__label", curie=PADI.curie('label'),
                   model_uri=PADI.authorityRecord__label, domain=None, range=str)

slots.authorityRecord__depth_index = Slot(uri=PADI.depth_index, name="authorityRecord__depth_index", curie=PADI.curie('depth_index'),
                   model_uri=PADI.authorityRecord__depth_index, domain=None, range=Union[str, "PadiDepth"])

slots.authorityRecord__source = Slot(uri=PADI.source, name="authorityRecord__source", curie=PADI.curie('source'),
                   model_uri=PADI.authorityRecord__source, domain=None, range=Optional[str])

slots.authorityRecord__status = Slot(uri=PADI.status, name="authorityRecord__status", curie=PADI.curie('status'),
                   model_uri=PADI.authorityRecord__status, domain=None, range=Optional[str])

slots.bureauAgent__id = Slot(uri=PADI.id, name="bureauAgent__id", curie=PADI.curie('id'),
                   model_uri=PADI.bureauAgent__id, domain=None, range=URIRef)

slots.bureauAgent__name = Slot(uri=PADI.name, name="bureauAgent__name", curie=PADI.curie('name'),
                   model_uri=PADI.bureauAgent__name, domain=None, range=str)

slots.bureauAgent__mandate = Slot(uri=PADI.mandate, name="bureauAgent__mandate", curie=PADI.curie('mandate'),
                   model_uri=PADI.bureauAgent__mandate, domain=None, range=Optional[str])

slots.outreachLog__id = Slot(uri=PADI.id, name="outreachLog__id", curie=PADI.curie('id'),
                   model_uri=PADI.outreachLog__id, domain=None, range=URIRef)

slots.outreachLog__target_node = Slot(uri=PADI.target_node, name="outreachLog__target_node", curie=PADI.curie('target_node'),
                   model_uri=PADI.outreachLog__target_node, domain=None, range=str)

slots.outreachLog__timestamp = Slot(uri=PADI.timestamp, name="outreachLog__timestamp", curie=PADI.curie('timestamp'),
                   model_uri=PADI.outreachLog__timestamp, domain=None, range=str)

slots.outreachLog__padi_depth_cited = Slot(uri=PADI.padi_depth_cited, name="outreachLog__padi_depth_cited", curie=PADI.curie('padi_depth_cited'),
                   model_uri=PADI.outreachLog__padi_depth_cited, domain=None, range=Optional[Union[str, "PadiDepth"]])

slots.outreachLog__outcome = Slot(uri=PADI.outcome, name="outreachLog__outcome", curie=PADI.curie('outcome'),
                   model_uri=PADI.outreachLog__outcome, domain=None, range=Optional[str])

