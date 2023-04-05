from typing import List, Optional

from sqlmodel import (
    Field,
    Relationship,
    SQLModel
)


class UnitFactionLink(SQLModel, table=True):
    __tablename__ = "unit_faction_links"

    unit_id: Optional[int] = Field(foreign_key="units.id", primary_key=True)
    unit_faction_id: Optional[int] = Field(
        foreign_key="unit_factions.id",
        primary_key=True
    )


class UnitAdvantageLink(SQLModel, table=True):
    __tablename__ = "unit_advantage_link"

    unit_id: Optional[int] = Field(foreign_key="units.id", primary_key=True)
    unit_advantange_id: Optional[int] = Field(
        foreign_key="unit_advantages.id",
        primary_key=True
    )


class UnitWeaponLink(SQLModel, table=True):
    __tablename__ = "unit_weapon_link"

    unit_id: Optional[int] = Field(foreign_key="units.id", primary_key=True)
    unit_weapon_id: Optional[int] = Field(
        foreign_key="unit_weapons.id",
        primary_key=True
    )


class Unit(SQLModel, table=True):
    __tablename__ = "units"

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    speed: Optional[int] = Field(default=None)
    strength: Optional[int] = Field(default=None)
    melee_attack: int
    ranged_attack: int
    defense: int
    armor: int
    focus: Optional[int] = Field(default=None)
    health: int
    deployment_cost: int

    types: List["UnitType"] = Relationship(back_populates="unit")
    factions: List["Faction"] = Relationship(
        back_populates="units",
        link_model=UnitFactionLink
    )
    advantages: List["Advantage"] = Relationship(
        back_populates="units",
        link_model=UnitAdvantageLink
    )
    weapons: List["Weapon"] = Relationship(
        back_populates="units",
        link_model=UnitWeaponLink
    )

    @property
    def spd(self) -> int:
        return self.spd

    @spd.setter
    def spd(self, spd: int) -> None:
        self.spd = spd

    @property
    def str(self) -> int:
        return self.str

    @str.setter
    def str(self, str: int) -> None:
        self.strength = str

    @property
    def mat(self) -> int:
        return self.melee_attack

    @mat.setter
    def mat(self, mat: int) -> None:
        self.melee_attack = mat

    @property
    def rat(self) -> int:
        return self.ranged_attack

    @rat.setter
    def rat(self, rat: int) -> None:
        self.ranged_attack = rat

    @property
    def arm(self) -> int:
        return self.armor

    @arm.setter
    def arm(self, arm: int) -> None:
        self.armor = arm

    @property
    def foc(self) -> int:
        return self.foc

    @foc.setter
    def arm(self, foc: int) -> None:
        self.focus = foc


class UnitType(SQLModel, table=True):
    __tablename__ = "unit_types"

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    unit_id: Optional[int] = Field(foreign_key="units.id")

    unit: "Unit" = Relationship(back_populates="types")


class Faction(SQLModel, table=True):
    __tablename__ = "unit_factions"

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str

    units: List["Unit"] = Relationship(
        back_populates="factions",
        link_model=UnitFactionLink
    )


class Advantage(SQLModel, table=True):
    __tablename__ = "unit_advantages"

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str

    units: List["Unit"] = Relationship(
        back_populates="advantages",
        link_model=UnitAdvantageLink
    )


class Weapon(SQLModel, table=True):
    __tablename__ = "unit_weapons"

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    range: int
    power: int
    type_id: Optional[int] = Field(foreign_key="weapon_types.id")
    quality_id: Optional[int] = Field(foreign_key="weapon_qualities.id")
    energy_type_id: Optional[int] = Field(foreign_key="weapon_energy_types.id")

    type: "WeaponType" = Relationship(back_populates="weapon")
    energy_type: "WeaponEnergyType" = Relationship(back_populates="weapon")
    quality: "WeaponQuality" = Relationship(back_populates="weapon")
    units: List["Unit"] = Relationship(
        back_populates="weapons",
        link_model=UnitWeaponLink
    )


class WeaponEnergyType(SQLModel, table=True):
    __tablename__ = "weapon_energy_types"

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str

    weapon: "Weapon" = Relationship(back_populates="energy_type")


class WeaponQuality(SQLModel, table=True):
    __tablename__ = "weapon_qualities"

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str

    weapon: "Weapon" = Relationship(back_populates="quality")


class WeaponType(SQLModel, table=True):
    __tablename__ = "weapon_types"

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str

    weapon: "Weapon" = Relationship(back_populates="type")