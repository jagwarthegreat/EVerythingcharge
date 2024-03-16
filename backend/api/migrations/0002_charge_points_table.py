"""charge_points_table

Revision ID: 0002
Revises: 0001
Create Date: 2024-03-15 17:39:02.463684

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0002'
down_revision = '0001'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('charge_points',
    sa.Column('description', sa.String(length=124), nullable=True),
    sa.Column('status', sa.String(), nullable=False),
    sa.Column('vendor', sa.String(), nullable=True),
    sa.Column('serial_number', sa.String(), nullable=True),
    sa.Column('location', sa.String(), nullable=True),
    sa.Column('model', sa.String(), nullable=True),
    sa.Column('ocpp_version', sa.String(), nullable=False),
    sa.Column('network_id', sa.String(), nullable=False),
    sa.Column('id', sa.String(length=20), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['network_id'], ['networks.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_charge_points_id'), 'charge_points', ['id'], unique=True)
    op.create_index(op.f('ix_charge_points_status'), 'charge_points', ['status'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_charge_points_status'), table_name='charge_points')
    op.drop_index(op.f('ix_charge_points_id'), table_name='charge_points')
    op.drop_table('charge_points')
    # ### end Alembic commands ###