"""make names unique for models

Revision ID: 9195f2137a84
Revises: 3016f45e7878
Create Date: 2023-04-07 23:54:01.136798

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision = '9195f2137a84'
down_revision = '3016f45e7878'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'unit_advantages', ['name'])
    op.create_unique_constraint(None, 'unit_factions', ['name'])
    op.create_unique_constraint(None, 'unit_types', ['name'])
    op.create_unique_constraint(None, 'unit_weapons', ['name'])
    op.create_unique_constraint(None, 'units', ['name'])
    op.create_unique_constraint(None, 'weapon_energy_types', ['name'])
    op.create_unique_constraint(None, 'weapon_qualities', ['name'])
    op.create_unique_constraint(None, 'weapon_types', ['name'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'weapon_types', type_='unique')
    op.drop_constraint(None, 'weapon_qualities', type_='unique')
    op.drop_constraint(None, 'weapon_energy_types', type_='unique')
    op.drop_constraint(None, 'units', type_='unique')
    op.drop_constraint(None, 'unit_weapons', type_='unique')
    op.drop_constraint(None, 'unit_types', type_='unique')
    op.drop_constraint(None, 'unit_factions', type_='unique')
    op.drop_constraint(None, 'unit_advantages', type_='unique')
    # ### end Alembic commands ###
