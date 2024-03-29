"""Initial Migration

Revision ID: 6995f4b86457
Revises: 
Create Date: 2023-04-04 23:28:58.298496

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision = '6995f4b86457'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('unit_advantages',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('unit_factions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('units',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('speed', sa.Integer(), nullable=True),
    sa.Column('strength', sa.Integer(), nullable=True),
    sa.Column('melee_attack', sa.Integer(), nullable=False),
    sa.Column('ranged_attack', sa.Integer(), nullable=False),
    sa.Column('defense', sa.Integer(), nullable=False),
    sa.Column('armor', sa.Integer(), nullable=False),
    sa.Column('focus', sa.Integer(), nullable=True),
    sa.Column('health', sa.Integer(), nullable=False),
    sa.Column('deployment_cost', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('weapon_energy_types',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('weapon_qualities',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('weapon_types',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('unit_advantage_link',
    sa.Column('unit_id', sa.Integer(), nullable=False),
    sa.Column('unit_advantange_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['unit_advantange_id'], ['unit_advantages.id'], ),
    sa.ForeignKeyConstraint(['unit_id'], ['units.id'], ),
    sa.PrimaryKeyConstraint('unit_id', 'unit_advantange_id')
    )
    op.create_table('unit_faction_links',
    sa.Column('unit_id', sa.Integer(), nullable=False),
    sa.Column('unit_faction_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['unit_faction_id'], ['unit_factions.id'], ),
    sa.ForeignKeyConstraint(['unit_id'], ['units.id'], ),
    sa.PrimaryKeyConstraint('unit_id', 'unit_faction_id')
    )
    op.create_table('unit_types',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('unit_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['unit_id'], ['units.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('unit_weapons',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('range', sa.Integer(), nullable=False),
    sa.Column('power', sa.Integer(), nullable=False),
    sa.Column('type_id', sa.Integer(), nullable=True),
    sa.Column('quality_id', sa.Integer(), nullable=True),
    sa.Column('energy_type_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['energy_type_id'], ['weapon_energy_types.id'], ),
    sa.ForeignKeyConstraint(['quality_id'], ['weapon_qualities.id'], ),
    sa.ForeignKeyConstraint(['type_id'], ['weapon_types.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('unit_weapon_link',
    sa.Column('unit_id', sa.Integer(), nullable=False),
    sa.Column('unit_weapon_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['unit_id'], ['units.id'], ),
    sa.ForeignKeyConstraint(['unit_weapon_id'], ['unit_weapons.id'], ),
    sa.PrimaryKeyConstraint('unit_id', 'unit_weapon_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('unit_weapon_link')
    op.drop_table('unit_weapons')
    op.drop_table('unit_types')
    op.drop_table('unit_faction_links')
    op.drop_table('unit_advantage_link')
    op.drop_table('weapon_types')
    op.drop_table('weapon_qualities')
    op.drop_table('weapon_energy_types')
    op.drop_table('units')
    op.drop_table('unit_factions')
    op.drop_table('unit_advantages')
    # ### end Alembic commands ###
