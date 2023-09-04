import sgqlc.types


zkbob_pool_schema = sgqlc.types.Schema()



########################################################################
# Scalars and Enumerations
########################################################################
class BigDecimal(sgqlc.types.Scalar):
    __schema__ = zkbob_pool_schema


class BigInt(sgqlc.types.Scalar):
    __schema__ = zkbob_pool_schema


Boolean = sgqlc.types.Boolean

class Bytes(sgqlc.types.Scalar):
    __schema__ = zkbob_pool_schema


class DDBatchOperation_orderBy(sgqlc.types.Enum):
    __schema__ = zkbob_pool_schema
    __choices__ = ('delegated_deposits', 'id', 'pooltx', 'pooltx__all_messages_hash', 'pooltx__calldata', 'pooltx__gas_used', 'pooltx__id', 'pooltx__index', 'pooltx__message', 'pooltx__ts', 'pooltx__tx', 'pooltx__type')


class DepositOperation_orderBy(sgqlc.types.Enum):
    __schema__ = zkbob_pool_schema
    __choices__ = ('fee', 'id', 'index_ref', 'nullifier', 'pooltx', 'pooltx__all_messages_hash', 'pooltx__calldata', 'pooltx__gas_used', 'pooltx__id', 'pooltx__index', 'pooltx__message', 'pooltx__ts', 'pooltx__tx', 'pooltx__type', 'token_amount')


class DirectDeposit_orderBy(sgqlc.types.Enum):
    __schema__ = zkbob_pool_schema
    __choices__ = ('bnClosed', 'bnInit', 'completed', 'deposit', 'fallbackUser', 'fee', 'id', 'index', 'payment', 'payment__id', 'payment__note', 'payment__sender', 'payment__token', 'pending', 'refunded', 'sender', 'tsClosed', 'tsInit', 'txClosed', 'txInit', 'zkAddress_diversifier', 'zkAddress_pk')


Float = sgqlc.types.Float

ID = sgqlc.types.ID

Int = sgqlc.types.Int

class Int8(sgqlc.types.Scalar):
    __schema__ = zkbob_pool_schema


class LastSyncBlock_orderBy(sgqlc.types.Enum):
    __schema__ = zkbob_pool_schema
    __choices__ = ('block', 'id')


class Operation_orderBy(sgqlc.types.Enum):
    __schema__ = zkbob_pool_schema
    __choices__ = ('id', 'pooltx', 'pooltx__all_messages_hash', 'pooltx__calldata', 'pooltx__gas_used', 'pooltx__id', 'pooltx__index', 'pooltx__message', 'pooltx__ts', 'pooltx__tx', 'pooltx__type')


class OrderDirection(sgqlc.types.Enum):
    __schema__ = zkbob_pool_schema
    __choices__ = ('asc', 'desc')


class Payment_orderBy(sgqlc.types.Enum):
    __schema__ = zkbob_pool_schema
    __choices__ = ('delegated_deposit', 'delegated_deposit__bnClosed', 'delegated_deposit__bnInit', 'delegated_deposit__completed', 'delegated_deposit__deposit', 'delegated_deposit__fallbackUser', 'delegated_deposit__fee', 'delegated_deposit__id', 'delegated_deposit__index', 'delegated_deposit__pending', 'delegated_deposit__refunded', 'delegated_deposit__sender', 'delegated_deposit__tsClosed', 'delegated_deposit__tsInit', 'delegated_deposit__txClosed', 'delegated_deposit__txInit', 'delegated_deposit__zkAddress_diversifier', 'delegated_deposit__zkAddress_pk', 'id', 'note', 'sender', 'token')


class PermittableDepositOperation_orderBy(sgqlc.types.Enum):
    __schema__ = zkbob_pool_schema
    __choices__ = ('fee', 'id', 'index_ref', 'nullifier', 'permit_deadline', 'permit_holder', 'pooltx', 'pooltx__all_messages_hash', 'pooltx__calldata', 'pooltx__gas_used', 'pooltx__id', 'pooltx__index', 'pooltx__message', 'pooltx__ts', 'pooltx__tx', 'pooltx__type', 'sig', 'token_amount')


class PoolTx_orderBy(sgqlc.types.Enum):
    __schema__ = zkbob_pool_schema
    __choices__ = ('all_messages_hash', 'calldata', 'gas_used', 'id', 'index', 'message', 'operation', 'operation__id', 'ts', 'tx', 'type', 'zk', 'zk__id', 'zk__out_commit', 'zk__tree_root_after')


String = sgqlc.types.String

class TransferOperation_orderBy(sgqlc.types.Enum):
    __schema__ = zkbob_pool_schema
    __choices__ = ('fee', 'id', 'index_ref', 'nullifier', 'pooltx', 'pooltx__all_messages_hash', 'pooltx__calldata', 'pooltx__gas_used', 'pooltx__id', 'pooltx__index', 'pooltx__message', 'pooltx__ts', 'pooltx__tx', 'pooltx__type')


class WithdrawalOperation_orderBy(sgqlc.types.Enum):
    __schema__ = zkbob_pool_schema
    __choices__ = ('energy_amount', 'fee', 'id', 'index_ref', 'native_amount', 'nullifier', 'pooltx', 'pooltx__all_messages_hash', 'pooltx__calldata', 'pooltx__gas_used', 'pooltx__id', 'pooltx__index', 'pooltx__message', 'pooltx__ts', 'pooltx__tx', 'pooltx__type', 'receiver', 'token_amount')


class ZkCommon_orderBy(sgqlc.types.Enum):
    __schema__ = zkbob_pool_schema
    __choices__ = ('id', 'out_commit', 'pooltx', 'pooltx__all_messages_hash', 'pooltx__calldata', 'pooltx__gas_used', 'pooltx__id', 'pooltx__index', 'pooltx__message', 'pooltx__ts', 'pooltx__tx', 'pooltx__type', 'tree_proof', 'tree_root_after', 'witness')


class _SubgraphErrorPolicy_(sgqlc.types.Enum):
    __schema__ = zkbob_pool_schema
    __choices__ = ('allow', 'deny')



########################################################################
# Input Objects
########################################################################
class BlockChangedFilter(sgqlc.types.Input):
    __schema__ = zkbob_pool_schema
    __field_names__ = ('number_gte',)
    number_gte = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='number_gte')


class Block_height(sgqlc.types.Input):
    __schema__ = zkbob_pool_schema
    __field_names__ = ('hash', 'number', 'number_gte')
    hash = sgqlc.types.Field(Bytes, graphql_name='hash')
    number = sgqlc.types.Field(Int, graphql_name='number')
    number_gte = sgqlc.types.Field(Int, graphql_name='number_gte')


class DDBatchOperation_filter(sgqlc.types.Input):
    __schema__ = zkbob_pool_schema
    __field_names__ = ('id', 'id_not', 'id_gt', 'id_lt', 'id_gte', 'id_lte', 'id_in', 'id_not_in', 'id_contains', 'id_contains_nocase', 'id_not_contains', 'id_not_contains_nocase', 'id_starts_with', 'id_starts_with_nocase', 'id_not_starts_with', 'id_not_starts_with_nocase', 'id_ends_with', 'id_ends_with_nocase', 'id_not_ends_with', 'id_not_ends_with_nocase', 'pooltx', 'pooltx_not', 'pooltx_gt', 'pooltx_lt', 'pooltx_gte', 'pooltx_lte', 'pooltx_in', 'pooltx_not_in', 'pooltx_contains', 'pooltx_contains_nocase', 'pooltx_not_contains', 'pooltx_not_contains_nocase', 'pooltx_starts_with', 'pooltx_starts_with_nocase', 'pooltx_not_starts_with', 'pooltx_not_starts_with_nocase', 'pooltx_ends_with', 'pooltx_ends_with_nocase', 'pooltx_not_ends_with', 'pooltx_not_ends_with_nocase', 'pooltx_', 'delegated_deposits', 'delegated_deposits_not', 'delegated_deposits_contains', 'delegated_deposits_contains_nocase', 'delegated_deposits_not_contains', 'delegated_deposits_not_contains_nocase', 'delegated_deposits_', '_change_block', 'and_', 'or_')
    id = sgqlc.types.Field(String, graphql_name='id')
    id_not = sgqlc.types.Field(String, graphql_name='id_not')
    id_gt = sgqlc.types.Field(String, graphql_name='id_gt')
    id_lt = sgqlc.types.Field(String, graphql_name='id_lt')
    id_gte = sgqlc.types.Field(String, graphql_name='id_gte')
    id_lte = sgqlc.types.Field(String, graphql_name='id_lte')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='id_not_in')
    id_contains = sgqlc.types.Field(String, graphql_name='id_contains')
    id_contains_nocase = sgqlc.types.Field(String, graphql_name='id_contains_nocase')
    id_not_contains = sgqlc.types.Field(String, graphql_name='id_not_contains')
    id_not_contains_nocase = sgqlc.types.Field(String, graphql_name='id_not_contains_nocase')
    id_starts_with = sgqlc.types.Field(String, graphql_name='id_starts_with')
    id_starts_with_nocase = sgqlc.types.Field(String, graphql_name='id_starts_with_nocase')
    id_not_starts_with = sgqlc.types.Field(String, graphql_name='id_not_starts_with')
    id_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='id_not_starts_with_nocase')
    id_ends_with = sgqlc.types.Field(String, graphql_name='id_ends_with')
    id_ends_with_nocase = sgqlc.types.Field(String, graphql_name='id_ends_with_nocase')
    id_not_ends_with = sgqlc.types.Field(String, graphql_name='id_not_ends_with')
    id_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='id_not_ends_with_nocase')
    pooltx = sgqlc.types.Field(String, graphql_name='pooltx')
    pooltx_not = sgqlc.types.Field(String, graphql_name='pooltx_not')
    pooltx_gt = sgqlc.types.Field(String, graphql_name='pooltx_gt')
    pooltx_lt = sgqlc.types.Field(String, graphql_name='pooltx_lt')
    pooltx_gte = sgqlc.types.Field(String, graphql_name='pooltx_gte')
    pooltx_lte = sgqlc.types.Field(String, graphql_name='pooltx_lte')
    pooltx_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='pooltx_in')
    pooltx_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='pooltx_not_in')
    pooltx_contains = sgqlc.types.Field(String, graphql_name='pooltx_contains')
    pooltx_contains_nocase = sgqlc.types.Field(String, graphql_name='pooltx_contains_nocase')
    pooltx_not_contains = sgqlc.types.Field(String, graphql_name='pooltx_not_contains')
    pooltx_not_contains_nocase = sgqlc.types.Field(String, graphql_name='pooltx_not_contains_nocase')
    pooltx_starts_with = sgqlc.types.Field(String, graphql_name='pooltx_starts_with')
    pooltx_starts_with_nocase = sgqlc.types.Field(String, graphql_name='pooltx_starts_with_nocase')
    pooltx_not_starts_with = sgqlc.types.Field(String, graphql_name='pooltx_not_starts_with')
    pooltx_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='pooltx_not_starts_with_nocase')
    pooltx_ends_with = sgqlc.types.Field(String, graphql_name='pooltx_ends_with')
    pooltx_ends_with_nocase = sgqlc.types.Field(String, graphql_name='pooltx_ends_with_nocase')
    pooltx_not_ends_with = sgqlc.types.Field(String, graphql_name='pooltx_not_ends_with')
    pooltx_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='pooltx_not_ends_with_nocase')
    pooltx_ = sgqlc.types.Field('PoolTx_filter', graphql_name='pooltx_')
    delegated_deposits = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='delegated_deposits')
    delegated_deposits_not = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='delegated_deposits_not')
    delegated_deposits_contains = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='delegated_deposits_contains')
    delegated_deposits_contains_nocase = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='delegated_deposits_contains_nocase')
    delegated_deposits_not_contains = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='delegated_deposits_not_contains')
    delegated_deposits_not_contains_nocase = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='delegated_deposits_not_contains_nocase')
    delegated_deposits_ = sgqlc.types.Field('DirectDeposit_filter', graphql_name='delegated_deposits_')
    _change_block = sgqlc.types.Field(BlockChangedFilter, graphql_name='_change_block')
    and_ = sgqlc.types.Field(sgqlc.types.list_of('DDBatchOperation_filter'), graphql_name='and')
    or_ = sgqlc.types.Field(sgqlc.types.list_of('DDBatchOperation_filter'), graphql_name='or')


class DepositOperation_filter(sgqlc.types.Input):
    __schema__ = zkbob_pool_schema
    __field_names__ = ('id', 'id_not', 'id_gt', 'id_lt', 'id_gte', 'id_lte', 'id_in', 'id_not_in', 'id_contains', 'id_contains_nocase', 'id_not_contains', 'id_not_contains_nocase', 'id_starts_with', 'id_starts_with_nocase', 'id_not_starts_with', 'id_not_starts_with_nocase', 'id_ends_with', 'id_ends_with_nocase', 'id_not_ends_with', 'id_not_ends_with_nocase', 'pooltx', 'pooltx_not', 'pooltx_gt', 'pooltx_lt', 'pooltx_gte', 'pooltx_lte', 'pooltx_in', 'pooltx_not_in', 'pooltx_contains', 'pooltx_contains_nocase', 'pooltx_not_contains', 'pooltx_not_contains_nocase', 'pooltx_starts_with', 'pooltx_starts_with_nocase', 'pooltx_not_starts_with', 'pooltx_not_starts_with_nocase', 'pooltx_ends_with', 'pooltx_ends_with_nocase', 'pooltx_not_ends_with', 'pooltx_not_ends_with_nocase', 'pooltx_', 'nullifier', 'nullifier_not', 'nullifier_gt', 'nullifier_lt', 'nullifier_gte', 'nullifier_lte', 'nullifier_in', 'nullifier_not_in', 'index_ref', 'index_ref_not', 'index_ref_gt', 'index_ref_lt', 'index_ref_gte', 'index_ref_lte', 'index_ref_in', 'index_ref_not_in', 'token_amount', 'token_amount_not', 'token_amount_gt', 'token_amount_lt', 'token_amount_gte', 'token_amount_lte', 'token_amount_in', 'token_amount_not_in', 'fee', 'fee_not', 'fee_gt', 'fee_lt', 'fee_gte', 'fee_lte', 'fee_in', 'fee_not_in', '_change_block', 'and_', 'or_')
    id = sgqlc.types.Field(String, graphql_name='id')
    id_not = sgqlc.types.Field(String, graphql_name='id_not')
    id_gt = sgqlc.types.Field(String, graphql_name='id_gt')
    id_lt = sgqlc.types.Field(String, graphql_name='id_lt')
    id_gte = sgqlc.types.Field(String, graphql_name='id_gte')
    id_lte = sgqlc.types.Field(String, graphql_name='id_lte')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='id_not_in')
    id_contains = sgqlc.types.Field(String, graphql_name='id_contains')
    id_contains_nocase = sgqlc.types.Field(String, graphql_name='id_contains_nocase')
    id_not_contains = sgqlc.types.Field(String, graphql_name='id_not_contains')
    id_not_contains_nocase = sgqlc.types.Field(String, graphql_name='id_not_contains_nocase')
    id_starts_with = sgqlc.types.Field(String, graphql_name='id_starts_with')
    id_starts_with_nocase = sgqlc.types.Field(String, graphql_name='id_starts_with_nocase')
    id_not_starts_with = sgqlc.types.Field(String, graphql_name='id_not_starts_with')
    id_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='id_not_starts_with_nocase')
    id_ends_with = sgqlc.types.Field(String, graphql_name='id_ends_with')
    id_ends_with_nocase = sgqlc.types.Field(String, graphql_name='id_ends_with_nocase')
    id_not_ends_with = sgqlc.types.Field(String, graphql_name='id_not_ends_with')
    id_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='id_not_ends_with_nocase')
    pooltx = sgqlc.types.Field(String, graphql_name='pooltx')
    pooltx_not = sgqlc.types.Field(String, graphql_name='pooltx_not')
    pooltx_gt = sgqlc.types.Field(String, graphql_name='pooltx_gt')
    pooltx_lt = sgqlc.types.Field(String, graphql_name='pooltx_lt')
    pooltx_gte = sgqlc.types.Field(String, graphql_name='pooltx_gte')
    pooltx_lte = sgqlc.types.Field(String, graphql_name='pooltx_lte')
    pooltx_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='pooltx_in')
    pooltx_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='pooltx_not_in')
    pooltx_contains = sgqlc.types.Field(String, graphql_name='pooltx_contains')
    pooltx_contains_nocase = sgqlc.types.Field(String, graphql_name='pooltx_contains_nocase')
    pooltx_not_contains = sgqlc.types.Field(String, graphql_name='pooltx_not_contains')
    pooltx_not_contains_nocase = sgqlc.types.Field(String, graphql_name='pooltx_not_contains_nocase')
    pooltx_starts_with = sgqlc.types.Field(String, graphql_name='pooltx_starts_with')
    pooltx_starts_with_nocase = sgqlc.types.Field(String, graphql_name='pooltx_starts_with_nocase')
    pooltx_not_starts_with = sgqlc.types.Field(String, graphql_name='pooltx_not_starts_with')
    pooltx_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='pooltx_not_starts_with_nocase')
    pooltx_ends_with = sgqlc.types.Field(String, graphql_name='pooltx_ends_with')
    pooltx_ends_with_nocase = sgqlc.types.Field(String, graphql_name='pooltx_ends_with_nocase')
    pooltx_not_ends_with = sgqlc.types.Field(String, graphql_name='pooltx_not_ends_with')
    pooltx_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='pooltx_not_ends_with_nocase')
    pooltx_ = sgqlc.types.Field('PoolTx_filter', graphql_name='pooltx_')
    nullifier = sgqlc.types.Field(BigInt, graphql_name='nullifier')
    nullifier_not = sgqlc.types.Field(BigInt, graphql_name='nullifier_not')
    nullifier_gt = sgqlc.types.Field(BigInt, graphql_name='nullifier_gt')
    nullifier_lt = sgqlc.types.Field(BigInt, graphql_name='nullifier_lt')
    nullifier_gte = sgqlc.types.Field(BigInt, graphql_name='nullifier_gte')
    nullifier_lte = sgqlc.types.Field(BigInt, graphql_name='nullifier_lte')
    nullifier_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='nullifier_in')
    nullifier_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='nullifier_not_in')
    index_ref = sgqlc.types.Field(BigInt, graphql_name='index_ref')
    index_ref_not = sgqlc.types.Field(BigInt, graphql_name='index_ref_not')
    index_ref_gt = sgqlc.types.Field(BigInt, graphql_name='index_ref_gt')
    index_ref_lt = sgqlc.types.Field(BigInt, graphql_name='index_ref_lt')
    index_ref_gte = sgqlc.types.Field(BigInt, graphql_name='index_ref_gte')
    index_ref_lte = sgqlc.types.Field(BigInt, graphql_name='index_ref_lte')
    index_ref_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='index_ref_in')
    index_ref_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='index_ref_not_in')
    token_amount = sgqlc.types.Field(BigInt, graphql_name='token_amount')
    token_amount_not = sgqlc.types.Field(BigInt, graphql_name='token_amount_not')
    token_amount_gt = sgqlc.types.Field(BigInt, graphql_name='token_amount_gt')
    token_amount_lt = sgqlc.types.Field(BigInt, graphql_name='token_amount_lt')
    token_amount_gte = sgqlc.types.Field(BigInt, graphql_name='token_amount_gte')
    token_amount_lte = sgqlc.types.Field(BigInt, graphql_name='token_amount_lte')
    token_amount_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='token_amount_in')
    token_amount_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='token_amount_not_in')
    fee = sgqlc.types.Field(BigInt, graphql_name='fee')
    fee_not = sgqlc.types.Field(BigInt, graphql_name='fee_not')
    fee_gt = sgqlc.types.Field(BigInt, graphql_name='fee_gt')
    fee_lt = sgqlc.types.Field(BigInt, graphql_name='fee_lt')
    fee_gte = sgqlc.types.Field(BigInt, graphql_name='fee_gte')
    fee_lte = sgqlc.types.Field(BigInt, graphql_name='fee_lte')
    fee_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='fee_in')
    fee_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='fee_not_in')
    _change_block = sgqlc.types.Field(BlockChangedFilter, graphql_name='_change_block')
    and_ = sgqlc.types.Field(sgqlc.types.list_of('DepositOperation_filter'), graphql_name='and')
    or_ = sgqlc.types.Field(sgqlc.types.list_of('DepositOperation_filter'), graphql_name='or')


class DirectDeposit_filter(sgqlc.types.Input):
    __schema__ = zkbob_pool_schema
    __field_names__ = ('id', 'id_not', 'id_gt', 'id_lt', 'id_gte', 'id_lte', 'id_in', 'id_not_in', 'id_contains', 'id_contains_nocase', 'id_not_contains', 'id_not_contains_nocase', 'id_starts_with', 'id_starts_with_nocase', 'id_not_starts_with', 'id_not_starts_with_nocase', 'id_ends_with', 'id_ends_with_nocase', 'id_not_ends_with', 'id_not_ends_with_nocase', 'index', 'index_not', 'index_gt', 'index_lt', 'index_gte', 'index_lte', 'index_in', 'index_not_in', 'pending', 'pending_not', 'pending_in', 'pending_not_in', 'completed', 'completed_not', 'completed_in', 'completed_not_in', 'refunded', 'refunded_not', 'refunded_in', 'refunded_not_in', 'sender', 'sender_not', 'sender_gt', 'sender_lt', 'sender_gte', 'sender_lte', 'sender_in', 'sender_not_in', 'sender_contains', 'sender_not_contains', 'fallback_user', 'fallback_user_not', 'fallback_user_gt', 'fallback_user_lt', 'fallback_user_gte', 'fallback_user_lte', 'fallback_user_in', 'fallback_user_not_in', 'fallback_user_contains', 'fallback_user_not_contains', 'zk_address_diversifier', 'zk_address_diversifier_not', 'zk_address_diversifier_gt', 'zk_address_diversifier_lt', 'zk_address_diversifier_gte', 'zk_address_diversifier_lte', 'zk_address_diversifier_in', 'zk_address_diversifier_not_in', 'zk_address_diversifier_contains', 'zk_address_diversifier_not_contains', 'zk_address_pk', 'zk_address_pk_not', 'zk_address_pk_gt', 'zk_address_pk_lt', 'zk_address_pk_gte', 'zk_address_pk_lte', 'zk_address_pk_in', 'zk_address_pk_not_in', 'zk_address_pk_contains', 'zk_address_pk_not_contains', 'deposit', 'deposit_not', 'deposit_gt', 'deposit_lt', 'deposit_gte', 'deposit_lte', 'deposit_in', 'deposit_not_in', 'fee', 'fee_not', 'fee_gt', 'fee_lt', 'fee_gte', 'fee_lte', 'fee_in', 'fee_not_in', 'bn_init', 'bn_init_not', 'bn_init_gt', 'bn_init_lt', 'bn_init_gte', 'bn_init_lte', 'bn_init_in', 'bn_init_not_in', 'ts_init', 'ts_init_not', 'ts_init_gt', 'ts_init_lt', 'ts_init_gte', 'ts_init_lte', 'ts_init_in', 'ts_init_not_in', 'tx_init', 'tx_init_not', 'tx_init_gt', 'tx_init_lt', 'tx_init_gte', 'tx_init_lte', 'tx_init_in', 'tx_init_not_in', 'tx_init_contains', 'tx_init_not_contains', 'payment', 'payment_not', 'payment_gt', 'payment_lt', 'payment_gte', 'payment_lte', 'payment_in', 'payment_not_in', 'payment_contains', 'payment_contains_nocase', 'payment_not_contains', 'payment_not_contains_nocase', 'payment_starts_with', 'payment_starts_with_nocase', 'payment_not_starts_with', 'payment_not_starts_with_nocase', 'payment_ends_with', 'payment_ends_with_nocase', 'payment_not_ends_with', 'payment_not_ends_with_nocase', 'payment_', 'bn_closed', 'bn_closed_not', 'bn_closed_gt', 'bn_closed_lt', 'bn_closed_gte', 'bn_closed_lte', 'bn_closed_in', 'bn_closed_not_in', 'ts_closed', 'ts_closed_not', 'ts_closed_gt', 'ts_closed_lt', 'ts_closed_gte', 'ts_closed_lte', 'ts_closed_in', 'ts_closed_not_in', 'tx_closed', 'tx_closed_not', 'tx_closed_gt', 'tx_closed_lt', 'tx_closed_gte', 'tx_closed_lte', 'tx_closed_in', 'tx_closed_not_in', 'tx_closed_contains', 'tx_closed_not_contains', '_change_block', 'and_', 'or_')
    id = sgqlc.types.Field(String, graphql_name='id')
    id_not = sgqlc.types.Field(String, graphql_name='id_not')
    id_gt = sgqlc.types.Field(String, graphql_name='id_gt')
    id_lt = sgqlc.types.Field(String, graphql_name='id_lt')
    id_gte = sgqlc.types.Field(String, graphql_name='id_gte')
    id_lte = sgqlc.types.Field(String, graphql_name='id_lte')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='id_not_in')
    id_contains = sgqlc.types.Field(String, graphql_name='id_contains')
    id_contains_nocase = sgqlc.types.Field(String, graphql_name='id_contains_nocase')
    id_not_contains = sgqlc.types.Field(String, graphql_name='id_not_contains')
    id_not_contains_nocase = sgqlc.types.Field(String, graphql_name='id_not_contains_nocase')
    id_starts_with = sgqlc.types.Field(String, graphql_name='id_starts_with')
    id_starts_with_nocase = sgqlc.types.Field(String, graphql_name='id_starts_with_nocase')
    id_not_starts_with = sgqlc.types.Field(String, graphql_name='id_not_starts_with')
    id_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='id_not_starts_with_nocase')
    id_ends_with = sgqlc.types.Field(String, graphql_name='id_ends_with')
    id_ends_with_nocase = sgqlc.types.Field(String, graphql_name='id_ends_with_nocase')
    id_not_ends_with = sgqlc.types.Field(String, graphql_name='id_not_ends_with')
    id_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='id_not_ends_with_nocase')
    index = sgqlc.types.Field(BigInt, graphql_name='index')
    index_not = sgqlc.types.Field(BigInt, graphql_name='index_not')
    index_gt = sgqlc.types.Field(BigInt, graphql_name='index_gt')
    index_lt = sgqlc.types.Field(BigInt, graphql_name='index_lt')
    index_gte = sgqlc.types.Field(BigInt, graphql_name='index_gte')
    index_lte = sgqlc.types.Field(BigInt, graphql_name='index_lte')
    index_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='index_in')
    index_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='index_not_in')
    pending = sgqlc.types.Field(Boolean, graphql_name='pending')
    pending_not = sgqlc.types.Field(Boolean, graphql_name='pending_not')
    pending_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Boolean)), graphql_name='pending_in')
    pending_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Boolean)), graphql_name='pending_not_in')
    completed = sgqlc.types.Field(Boolean, graphql_name='completed')
    completed_not = sgqlc.types.Field(Boolean, graphql_name='completed_not')
    completed_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Boolean)), graphql_name='completed_in')
    completed_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Boolean)), graphql_name='completed_not_in')
    refunded = sgqlc.types.Field(Boolean, graphql_name='refunded')
    refunded_not = sgqlc.types.Field(Boolean, graphql_name='refunded_not')
    refunded_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Boolean)), graphql_name='refunded_in')
    refunded_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Boolean)), graphql_name='refunded_not_in')
    sender = sgqlc.types.Field(Bytes, graphql_name='sender')
    sender_not = sgqlc.types.Field(Bytes, graphql_name='sender_not')
    sender_gt = sgqlc.types.Field(Bytes, graphql_name='sender_gt')
    sender_lt = sgqlc.types.Field(Bytes, graphql_name='sender_lt')
    sender_gte = sgqlc.types.Field(Bytes, graphql_name='sender_gte')
    sender_lte = sgqlc.types.Field(Bytes, graphql_name='sender_lte')
    sender_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='sender_in')
    sender_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='sender_not_in')
    sender_contains = sgqlc.types.Field(Bytes, graphql_name='sender_contains')
    sender_not_contains = sgqlc.types.Field(Bytes, graphql_name='sender_not_contains')
    fallback_user = sgqlc.types.Field(Bytes, graphql_name='fallbackUser')
    fallback_user_not = sgqlc.types.Field(Bytes, graphql_name='fallbackUser_not')
    fallback_user_gt = sgqlc.types.Field(Bytes, graphql_name='fallbackUser_gt')
    fallback_user_lt = sgqlc.types.Field(Bytes, graphql_name='fallbackUser_lt')
    fallback_user_gte = sgqlc.types.Field(Bytes, graphql_name='fallbackUser_gte')
    fallback_user_lte = sgqlc.types.Field(Bytes, graphql_name='fallbackUser_lte')
    fallback_user_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='fallbackUser_in')
    fallback_user_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='fallbackUser_not_in')
    fallback_user_contains = sgqlc.types.Field(Bytes, graphql_name='fallbackUser_contains')
    fallback_user_not_contains = sgqlc.types.Field(Bytes, graphql_name='fallbackUser_not_contains')
    zk_address_diversifier = sgqlc.types.Field(Bytes, graphql_name='zkAddress_diversifier')
    zk_address_diversifier_not = sgqlc.types.Field(Bytes, graphql_name='zkAddress_diversifier_not')
    zk_address_diversifier_gt = sgqlc.types.Field(Bytes, graphql_name='zkAddress_diversifier_gt')
    zk_address_diversifier_lt = sgqlc.types.Field(Bytes, graphql_name='zkAddress_diversifier_lt')
    zk_address_diversifier_gte = sgqlc.types.Field(Bytes, graphql_name='zkAddress_diversifier_gte')
    zk_address_diversifier_lte = sgqlc.types.Field(Bytes, graphql_name='zkAddress_diversifier_lte')
    zk_address_diversifier_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='zkAddress_diversifier_in')
    zk_address_diversifier_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='zkAddress_diversifier_not_in')
    zk_address_diversifier_contains = sgqlc.types.Field(Bytes, graphql_name='zkAddress_diversifier_contains')
    zk_address_diversifier_not_contains = sgqlc.types.Field(Bytes, graphql_name='zkAddress_diversifier_not_contains')
    zk_address_pk = sgqlc.types.Field(Bytes, graphql_name='zkAddress_pk')
    zk_address_pk_not = sgqlc.types.Field(Bytes, graphql_name='zkAddress_pk_not')
    zk_address_pk_gt = sgqlc.types.Field(Bytes, graphql_name='zkAddress_pk_gt')
    zk_address_pk_lt = sgqlc.types.Field(Bytes, graphql_name='zkAddress_pk_lt')
    zk_address_pk_gte = sgqlc.types.Field(Bytes, graphql_name='zkAddress_pk_gte')
    zk_address_pk_lte = sgqlc.types.Field(Bytes, graphql_name='zkAddress_pk_lte')
    zk_address_pk_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='zkAddress_pk_in')
    zk_address_pk_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='zkAddress_pk_not_in')
    zk_address_pk_contains = sgqlc.types.Field(Bytes, graphql_name='zkAddress_pk_contains')
    zk_address_pk_not_contains = sgqlc.types.Field(Bytes, graphql_name='zkAddress_pk_not_contains')
    deposit = sgqlc.types.Field(BigInt, graphql_name='deposit')
    deposit_not = sgqlc.types.Field(BigInt, graphql_name='deposit_not')
    deposit_gt = sgqlc.types.Field(BigInt, graphql_name='deposit_gt')
    deposit_lt = sgqlc.types.Field(BigInt, graphql_name='deposit_lt')
    deposit_gte = sgqlc.types.Field(BigInt, graphql_name='deposit_gte')
    deposit_lte = sgqlc.types.Field(BigInt, graphql_name='deposit_lte')
    deposit_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='deposit_in')
    deposit_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='deposit_not_in')
    fee = sgqlc.types.Field(BigInt, graphql_name='fee')
    fee_not = sgqlc.types.Field(BigInt, graphql_name='fee_not')
    fee_gt = sgqlc.types.Field(BigInt, graphql_name='fee_gt')
    fee_lt = sgqlc.types.Field(BigInt, graphql_name='fee_lt')
    fee_gte = sgqlc.types.Field(BigInt, graphql_name='fee_gte')
    fee_lte = sgqlc.types.Field(BigInt, graphql_name='fee_lte')
    fee_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='fee_in')
    fee_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='fee_not_in')
    bn_init = sgqlc.types.Field(BigInt, graphql_name='bnInit')
    bn_init_not = sgqlc.types.Field(BigInt, graphql_name='bnInit_not')
    bn_init_gt = sgqlc.types.Field(BigInt, graphql_name='bnInit_gt')
    bn_init_lt = sgqlc.types.Field(BigInt, graphql_name='bnInit_lt')
    bn_init_gte = sgqlc.types.Field(BigInt, graphql_name='bnInit_gte')
    bn_init_lte = sgqlc.types.Field(BigInt, graphql_name='bnInit_lte')
    bn_init_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='bnInit_in')
    bn_init_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='bnInit_not_in')
    ts_init = sgqlc.types.Field(BigInt, graphql_name='tsInit')
    ts_init_not = sgqlc.types.Field(BigInt, graphql_name='tsInit_not')
    ts_init_gt = sgqlc.types.Field(BigInt, graphql_name='tsInit_gt')
    ts_init_lt = sgqlc.types.Field(BigInt, graphql_name='tsInit_lt')
    ts_init_gte = sgqlc.types.Field(BigInt, graphql_name='tsInit_gte')
    ts_init_lte = sgqlc.types.Field(BigInt, graphql_name='tsInit_lte')
    ts_init_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='tsInit_in')
    ts_init_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='tsInit_not_in')
    tx_init = sgqlc.types.Field(Bytes, graphql_name='txInit')
    tx_init_not = sgqlc.types.Field(Bytes, graphql_name='txInit_not')
    tx_init_gt = sgqlc.types.Field(Bytes, graphql_name='txInit_gt')
    tx_init_lt = sgqlc.types.Field(Bytes, graphql_name='txInit_lt')
    tx_init_gte = sgqlc.types.Field(Bytes, graphql_name='txInit_gte')
    tx_init_lte = sgqlc.types.Field(Bytes, graphql_name='txInit_lte')
    tx_init_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='txInit_in')
    tx_init_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='txInit_not_in')
    tx_init_contains = sgqlc.types.Field(Bytes, graphql_name='txInit_contains')
    tx_init_not_contains = sgqlc.types.Field(Bytes, graphql_name='txInit_not_contains')
    payment = sgqlc.types.Field(String, graphql_name='payment')
    payment_not = sgqlc.types.Field(String, graphql_name='payment_not')
    payment_gt = sgqlc.types.Field(String, graphql_name='payment_gt')
    payment_lt = sgqlc.types.Field(String, graphql_name='payment_lt')
    payment_gte = sgqlc.types.Field(String, graphql_name='payment_gte')
    payment_lte = sgqlc.types.Field(String, graphql_name='payment_lte')
    payment_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='payment_in')
    payment_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='payment_not_in')
    payment_contains = sgqlc.types.Field(String, graphql_name='payment_contains')
    payment_contains_nocase = sgqlc.types.Field(String, graphql_name='payment_contains_nocase')
    payment_not_contains = sgqlc.types.Field(String, graphql_name='payment_not_contains')
    payment_not_contains_nocase = sgqlc.types.Field(String, graphql_name='payment_not_contains_nocase')
    payment_starts_with = sgqlc.types.Field(String, graphql_name='payment_starts_with')
    payment_starts_with_nocase = sgqlc.types.Field(String, graphql_name='payment_starts_with_nocase')
    payment_not_starts_with = sgqlc.types.Field(String, graphql_name='payment_not_starts_with')
    payment_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='payment_not_starts_with_nocase')
    payment_ends_with = sgqlc.types.Field(String, graphql_name='payment_ends_with')
    payment_ends_with_nocase = sgqlc.types.Field(String, graphql_name='payment_ends_with_nocase')
    payment_not_ends_with = sgqlc.types.Field(String, graphql_name='payment_not_ends_with')
    payment_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='payment_not_ends_with_nocase')
    payment_ = sgqlc.types.Field('Payment_filter', graphql_name='payment_')
    bn_closed = sgqlc.types.Field(BigInt, graphql_name='bnClosed')
    bn_closed_not = sgqlc.types.Field(BigInt, graphql_name='bnClosed_not')
    bn_closed_gt = sgqlc.types.Field(BigInt, graphql_name='bnClosed_gt')
    bn_closed_lt = sgqlc.types.Field(BigInt, graphql_name='bnClosed_lt')
    bn_closed_gte = sgqlc.types.Field(BigInt, graphql_name='bnClosed_gte')
    bn_closed_lte = sgqlc.types.Field(BigInt, graphql_name='bnClosed_lte')
    bn_closed_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='bnClosed_in')
    bn_closed_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='bnClosed_not_in')
    ts_closed = sgqlc.types.Field(BigInt, graphql_name='tsClosed')
    ts_closed_not = sgqlc.types.Field(BigInt, graphql_name='tsClosed_not')
    ts_closed_gt = sgqlc.types.Field(BigInt, graphql_name='tsClosed_gt')
    ts_closed_lt = sgqlc.types.Field(BigInt, graphql_name='tsClosed_lt')
    ts_closed_gte = sgqlc.types.Field(BigInt, graphql_name='tsClosed_gte')
    ts_closed_lte = sgqlc.types.Field(BigInt, graphql_name='tsClosed_lte')
    ts_closed_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='tsClosed_in')
    ts_closed_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='tsClosed_not_in')
    tx_closed = sgqlc.types.Field(Bytes, graphql_name='txClosed')
    tx_closed_not = sgqlc.types.Field(Bytes, graphql_name='txClosed_not')
    tx_closed_gt = sgqlc.types.Field(Bytes, graphql_name='txClosed_gt')
    tx_closed_lt = sgqlc.types.Field(Bytes, graphql_name='txClosed_lt')
    tx_closed_gte = sgqlc.types.Field(Bytes, graphql_name='txClosed_gte')
    tx_closed_lte = sgqlc.types.Field(Bytes, graphql_name='txClosed_lte')
    tx_closed_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='txClosed_in')
    tx_closed_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='txClosed_not_in')
    tx_closed_contains = sgqlc.types.Field(Bytes, graphql_name='txClosed_contains')
    tx_closed_not_contains = sgqlc.types.Field(Bytes, graphql_name='txClosed_not_contains')
    _change_block = sgqlc.types.Field(BlockChangedFilter, graphql_name='_change_block')
    and_ = sgqlc.types.Field(sgqlc.types.list_of('DirectDeposit_filter'), graphql_name='and')
    or_ = sgqlc.types.Field(sgqlc.types.list_of('DirectDeposit_filter'), graphql_name='or')


class LastSyncBlock_filter(sgqlc.types.Input):
    __schema__ = zkbob_pool_schema
    __field_names__ = ('id', 'id_not', 'id_gt', 'id_lt', 'id_gte', 'id_lte', 'id_in', 'id_not_in', 'id_contains', 'id_not_contains', 'block', 'block_not', 'block_gt', 'block_lt', 'block_gte', 'block_lte', 'block_in', 'block_not_in', '_change_block', 'and_', 'or_')
    id = sgqlc.types.Field(Bytes, graphql_name='id')
    id_not = sgqlc.types.Field(Bytes, graphql_name='id_not')
    id_gt = sgqlc.types.Field(Bytes, graphql_name='id_gt')
    id_lt = sgqlc.types.Field(Bytes, graphql_name='id_lt')
    id_gte = sgqlc.types.Field(Bytes, graphql_name='id_gte')
    id_lte = sgqlc.types.Field(Bytes, graphql_name='id_lte')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='id_not_in')
    id_contains = sgqlc.types.Field(Bytes, graphql_name='id_contains')
    id_not_contains = sgqlc.types.Field(Bytes, graphql_name='id_not_contains')
    block = sgqlc.types.Field(BigInt, graphql_name='block')
    block_not = sgqlc.types.Field(BigInt, graphql_name='block_not')
    block_gt = sgqlc.types.Field(BigInt, graphql_name='block_gt')
    block_lt = sgqlc.types.Field(BigInt, graphql_name='block_lt')
    block_gte = sgqlc.types.Field(BigInt, graphql_name='block_gte')
    block_lte = sgqlc.types.Field(BigInt, graphql_name='block_lte')
    block_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='block_in')
    block_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='block_not_in')
    _change_block = sgqlc.types.Field(BlockChangedFilter, graphql_name='_change_block')
    and_ = sgqlc.types.Field(sgqlc.types.list_of('LastSyncBlock_filter'), graphql_name='and')
    or_ = sgqlc.types.Field(sgqlc.types.list_of('LastSyncBlock_filter'), graphql_name='or')


class Operation_filter(sgqlc.types.Input):
    __schema__ = zkbob_pool_schema
    __field_names__ = ('id', 'id_not', 'id_gt', 'id_lt', 'id_gte', 'id_lte', 'id_in', 'id_not_in', 'id_contains', 'id_contains_nocase', 'id_not_contains', 'id_not_contains_nocase', 'id_starts_with', 'id_starts_with_nocase', 'id_not_starts_with', 'id_not_starts_with_nocase', 'id_ends_with', 'id_ends_with_nocase', 'id_not_ends_with', 'id_not_ends_with_nocase', 'pooltx', 'pooltx_not', 'pooltx_gt', 'pooltx_lt', 'pooltx_gte', 'pooltx_lte', 'pooltx_in', 'pooltx_not_in', 'pooltx_contains', 'pooltx_contains_nocase', 'pooltx_not_contains', 'pooltx_not_contains_nocase', 'pooltx_starts_with', 'pooltx_starts_with_nocase', 'pooltx_not_starts_with', 'pooltx_not_starts_with_nocase', 'pooltx_ends_with', 'pooltx_ends_with_nocase', 'pooltx_not_ends_with', 'pooltx_not_ends_with_nocase', 'pooltx_', '_change_block', 'and_', 'or_')
    id = sgqlc.types.Field(String, graphql_name='id')
    id_not = sgqlc.types.Field(String, graphql_name='id_not')
    id_gt = sgqlc.types.Field(String, graphql_name='id_gt')
    id_lt = sgqlc.types.Field(String, graphql_name='id_lt')
    id_gte = sgqlc.types.Field(String, graphql_name='id_gte')
    id_lte = sgqlc.types.Field(String, graphql_name='id_lte')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='id_not_in')
    id_contains = sgqlc.types.Field(String, graphql_name='id_contains')
    id_contains_nocase = sgqlc.types.Field(String, graphql_name='id_contains_nocase')
    id_not_contains = sgqlc.types.Field(String, graphql_name='id_not_contains')
    id_not_contains_nocase = sgqlc.types.Field(String, graphql_name='id_not_contains_nocase')
    id_starts_with = sgqlc.types.Field(String, graphql_name='id_starts_with')
    id_starts_with_nocase = sgqlc.types.Field(String, graphql_name='id_starts_with_nocase')
    id_not_starts_with = sgqlc.types.Field(String, graphql_name='id_not_starts_with')
    id_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='id_not_starts_with_nocase')
    id_ends_with = sgqlc.types.Field(String, graphql_name='id_ends_with')
    id_ends_with_nocase = sgqlc.types.Field(String, graphql_name='id_ends_with_nocase')
    id_not_ends_with = sgqlc.types.Field(String, graphql_name='id_not_ends_with')
    id_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='id_not_ends_with_nocase')
    pooltx = sgqlc.types.Field(String, graphql_name='pooltx')
    pooltx_not = sgqlc.types.Field(String, graphql_name='pooltx_not')
    pooltx_gt = sgqlc.types.Field(String, graphql_name='pooltx_gt')
    pooltx_lt = sgqlc.types.Field(String, graphql_name='pooltx_lt')
    pooltx_gte = sgqlc.types.Field(String, graphql_name='pooltx_gte')
    pooltx_lte = sgqlc.types.Field(String, graphql_name='pooltx_lte')
    pooltx_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='pooltx_in')
    pooltx_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='pooltx_not_in')
    pooltx_contains = sgqlc.types.Field(String, graphql_name='pooltx_contains')
    pooltx_contains_nocase = sgqlc.types.Field(String, graphql_name='pooltx_contains_nocase')
    pooltx_not_contains = sgqlc.types.Field(String, graphql_name='pooltx_not_contains')
    pooltx_not_contains_nocase = sgqlc.types.Field(String, graphql_name='pooltx_not_contains_nocase')
    pooltx_starts_with = sgqlc.types.Field(String, graphql_name='pooltx_starts_with')
    pooltx_starts_with_nocase = sgqlc.types.Field(String, graphql_name='pooltx_starts_with_nocase')
    pooltx_not_starts_with = sgqlc.types.Field(String, graphql_name='pooltx_not_starts_with')
    pooltx_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='pooltx_not_starts_with_nocase')
    pooltx_ends_with = sgqlc.types.Field(String, graphql_name='pooltx_ends_with')
    pooltx_ends_with_nocase = sgqlc.types.Field(String, graphql_name='pooltx_ends_with_nocase')
    pooltx_not_ends_with = sgqlc.types.Field(String, graphql_name='pooltx_not_ends_with')
    pooltx_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='pooltx_not_ends_with_nocase')
    pooltx_ = sgqlc.types.Field('PoolTx_filter', graphql_name='pooltx_')
    _change_block = sgqlc.types.Field(BlockChangedFilter, graphql_name='_change_block')
    and_ = sgqlc.types.Field(sgqlc.types.list_of('Operation_filter'), graphql_name='and')
    or_ = sgqlc.types.Field(sgqlc.types.list_of('Operation_filter'), graphql_name='or')


class Payment_filter(sgqlc.types.Input):
    __schema__ = zkbob_pool_schema
    __field_names__ = ('id', 'id_not', 'id_gt', 'id_lt', 'id_gte', 'id_lte', 'id_in', 'id_not_in', 'id_contains', 'id_contains_nocase', 'id_not_contains', 'id_not_contains_nocase', 'id_starts_with', 'id_starts_with_nocase', 'id_not_starts_with', 'id_not_starts_with_nocase', 'id_ends_with', 'id_ends_with_nocase', 'id_not_ends_with', 'id_not_ends_with_nocase', 'sender', 'sender_not', 'sender_gt', 'sender_lt', 'sender_gte', 'sender_lte', 'sender_in', 'sender_not_in', 'sender_contains', 'sender_not_contains', 'delegated_deposit', 'delegated_deposit_not', 'delegated_deposit_gt', 'delegated_deposit_lt', 'delegated_deposit_gte', 'delegated_deposit_lte', 'delegated_deposit_in', 'delegated_deposit_not_in', 'delegated_deposit_contains', 'delegated_deposit_contains_nocase', 'delegated_deposit_not_contains', 'delegated_deposit_not_contains_nocase', 'delegated_deposit_starts_with', 'delegated_deposit_starts_with_nocase', 'delegated_deposit_not_starts_with', 'delegated_deposit_not_starts_with_nocase', 'delegated_deposit_ends_with', 'delegated_deposit_ends_with_nocase', 'delegated_deposit_not_ends_with', 'delegated_deposit_not_ends_with_nocase', 'delegated_deposit_', 'token', 'token_not', 'token_gt', 'token_lt', 'token_gte', 'token_lte', 'token_in', 'token_not_in', 'token_contains', 'token_not_contains', 'note', 'note_not', 'note_gt', 'note_lt', 'note_gte', 'note_lte', 'note_in', 'note_not_in', 'note_contains', 'note_not_contains', '_change_block', 'and_', 'or_')
    id = sgqlc.types.Field(String, graphql_name='id')
    id_not = sgqlc.types.Field(String, graphql_name='id_not')
    id_gt = sgqlc.types.Field(String, graphql_name='id_gt')
    id_lt = sgqlc.types.Field(String, graphql_name='id_lt')
    id_gte = sgqlc.types.Field(String, graphql_name='id_gte')
    id_lte = sgqlc.types.Field(String, graphql_name='id_lte')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='id_not_in')
    id_contains = sgqlc.types.Field(String, graphql_name='id_contains')
    id_contains_nocase = sgqlc.types.Field(String, graphql_name='id_contains_nocase')
    id_not_contains = sgqlc.types.Field(String, graphql_name='id_not_contains')
    id_not_contains_nocase = sgqlc.types.Field(String, graphql_name='id_not_contains_nocase')
    id_starts_with = sgqlc.types.Field(String, graphql_name='id_starts_with')
    id_starts_with_nocase = sgqlc.types.Field(String, graphql_name='id_starts_with_nocase')
    id_not_starts_with = sgqlc.types.Field(String, graphql_name='id_not_starts_with')
    id_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='id_not_starts_with_nocase')
    id_ends_with = sgqlc.types.Field(String, graphql_name='id_ends_with')
    id_ends_with_nocase = sgqlc.types.Field(String, graphql_name='id_ends_with_nocase')
    id_not_ends_with = sgqlc.types.Field(String, graphql_name='id_not_ends_with')
    id_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='id_not_ends_with_nocase')
    sender = sgqlc.types.Field(Bytes, graphql_name='sender')
    sender_not = sgqlc.types.Field(Bytes, graphql_name='sender_not')
    sender_gt = sgqlc.types.Field(Bytes, graphql_name='sender_gt')
    sender_lt = sgqlc.types.Field(Bytes, graphql_name='sender_lt')
    sender_gte = sgqlc.types.Field(Bytes, graphql_name='sender_gte')
    sender_lte = sgqlc.types.Field(Bytes, graphql_name='sender_lte')
    sender_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='sender_in')
    sender_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='sender_not_in')
    sender_contains = sgqlc.types.Field(Bytes, graphql_name='sender_contains')
    sender_not_contains = sgqlc.types.Field(Bytes, graphql_name='sender_not_contains')
    delegated_deposit = sgqlc.types.Field(String, graphql_name='delegated_deposit')
    delegated_deposit_not = sgqlc.types.Field(String, graphql_name='delegated_deposit_not')
    delegated_deposit_gt = sgqlc.types.Field(String, graphql_name='delegated_deposit_gt')
    delegated_deposit_lt = sgqlc.types.Field(String, graphql_name='delegated_deposit_lt')
    delegated_deposit_gte = sgqlc.types.Field(String, graphql_name='delegated_deposit_gte')
    delegated_deposit_lte = sgqlc.types.Field(String, graphql_name='delegated_deposit_lte')
    delegated_deposit_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='delegated_deposit_in')
    delegated_deposit_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='delegated_deposit_not_in')
    delegated_deposit_contains = sgqlc.types.Field(String, graphql_name='delegated_deposit_contains')
    delegated_deposit_contains_nocase = sgqlc.types.Field(String, graphql_name='delegated_deposit_contains_nocase')
    delegated_deposit_not_contains = sgqlc.types.Field(String, graphql_name='delegated_deposit_not_contains')
    delegated_deposit_not_contains_nocase = sgqlc.types.Field(String, graphql_name='delegated_deposit_not_contains_nocase')
    delegated_deposit_starts_with = sgqlc.types.Field(String, graphql_name='delegated_deposit_starts_with')
    delegated_deposit_starts_with_nocase = sgqlc.types.Field(String, graphql_name='delegated_deposit_starts_with_nocase')
    delegated_deposit_not_starts_with = sgqlc.types.Field(String, graphql_name='delegated_deposit_not_starts_with')
    delegated_deposit_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='delegated_deposit_not_starts_with_nocase')
    delegated_deposit_ends_with = sgqlc.types.Field(String, graphql_name='delegated_deposit_ends_with')
    delegated_deposit_ends_with_nocase = sgqlc.types.Field(String, graphql_name='delegated_deposit_ends_with_nocase')
    delegated_deposit_not_ends_with = sgqlc.types.Field(String, graphql_name='delegated_deposit_not_ends_with')
    delegated_deposit_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='delegated_deposit_not_ends_with_nocase')
    delegated_deposit_ = sgqlc.types.Field(DirectDeposit_filter, graphql_name='delegated_deposit_')
    token = sgqlc.types.Field(Bytes, graphql_name='token')
    token_not = sgqlc.types.Field(Bytes, graphql_name='token_not')
    token_gt = sgqlc.types.Field(Bytes, graphql_name='token_gt')
    token_lt = sgqlc.types.Field(Bytes, graphql_name='token_lt')
    token_gte = sgqlc.types.Field(Bytes, graphql_name='token_gte')
    token_lte = sgqlc.types.Field(Bytes, graphql_name='token_lte')
    token_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='token_in')
    token_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='token_not_in')
    token_contains = sgqlc.types.Field(Bytes, graphql_name='token_contains')
    token_not_contains = sgqlc.types.Field(Bytes, graphql_name='token_not_contains')
    note = sgqlc.types.Field(Bytes, graphql_name='note')
    note_not = sgqlc.types.Field(Bytes, graphql_name='note_not')
    note_gt = sgqlc.types.Field(Bytes, graphql_name='note_gt')
    note_lt = sgqlc.types.Field(Bytes, graphql_name='note_lt')
    note_gte = sgqlc.types.Field(Bytes, graphql_name='note_gte')
    note_lte = sgqlc.types.Field(Bytes, graphql_name='note_lte')
    note_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='note_in')
    note_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='note_not_in')
    note_contains = sgqlc.types.Field(Bytes, graphql_name='note_contains')
    note_not_contains = sgqlc.types.Field(Bytes, graphql_name='note_not_contains')
    _change_block = sgqlc.types.Field(BlockChangedFilter, graphql_name='_change_block')
    and_ = sgqlc.types.Field(sgqlc.types.list_of('Payment_filter'), graphql_name='and')
    or_ = sgqlc.types.Field(sgqlc.types.list_of('Payment_filter'), graphql_name='or')


class PermittableDepositOperation_filter(sgqlc.types.Input):
    __schema__ = zkbob_pool_schema
    __field_names__ = ('id', 'id_not', 'id_gt', 'id_lt', 'id_gte', 'id_lte', 'id_in', 'id_not_in', 'id_contains', 'id_contains_nocase', 'id_not_contains', 'id_not_contains_nocase', 'id_starts_with', 'id_starts_with_nocase', 'id_not_starts_with', 'id_not_starts_with_nocase', 'id_ends_with', 'id_ends_with_nocase', 'id_not_ends_with', 'id_not_ends_with_nocase', 'pooltx', 'pooltx_not', 'pooltx_gt', 'pooltx_lt', 'pooltx_gte', 'pooltx_lte', 'pooltx_in', 'pooltx_not_in', 'pooltx_contains', 'pooltx_contains_nocase', 'pooltx_not_contains', 'pooltx_not_contains_nocase', 'pooltx_starts_with', 'pooltx_starts_with_nocase', 'pooltx_not_starts_with', 'pooltx_not_starts_with_nocase', 'pooltx_ends_with', 'pooltx_ends_with_nocase', 'pooltx_not_ends_with', 'pooltx_not_ends_with_nocase', 'pooltx_', 'nullifier', 'nullifier_not', 'nullifier_gt', 'nullifier_lt', 'nullifier_gte', 'nullifier_lte', 'nullifier_in', 'nullifier_not_in', 'index_ref', 'index_ref_not', 'index_ref_gt', 'index_ref_lt', 'index_ref_gte', 'index_ref_lte', 'index_ref_in', 'index_ref_not_in', 'token_amount', 'token_amount_not', 'token_amount_gt', 'token_amount_lt', 'token_amount_gte', 'token_amount_lte', 'token_amount_in', 'token_amount_not_in', 'fee', 'fee_not', 'fee_gt', 'fee_lt', 'fee_gte', 'fee_lte', 'fee_in', 'fee_not_in', 'permit_deadline', 'permit_deadline_not', 'permit_deadline_gt', 'permit_deadline_lt', 'permit_deadline_gte', 'permit_deadline_lte', 'permit_deadline_in', 'permit_deadline_not_in', 'permit_holder', 'permit_holder_not', 'permit_holder_gt', 'permit_holder_lt', 'permit_holder_gte', 'permit_holder_lte', 'permit_holder_in', 'permit_holder_not_in', 'permit_holder_contains', 'permit_holder_not_contains', 'sig', 'sig_not', 'sig_gt', 'sig_lt', 'sig_gte', 'sig_lte', 'sig_in', 'sig_not_in', 'sig_contains', 'sig_not_contains', '_change_block', 'and_', 'or_')
    id = sgqlc.types.Field(String, graphql_name='id')
    id_not = sgqlc.types.Field(String, graphql_name='id_not')
    id_gt = sgqlc.types.Field(String, graphql_name='id_gt')
    id_lt = sgqlc.types.Field(String, graphql_name='id_lt')
    id_gte = sgqlc.types.Field(String, graphql_name='id_gte')
    id_lte = sgqlc.types.Field(String, graphql_name='id_lte')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='id_not_in')
    id_contains = sgqlc.types.Field(String, graphql_name='id_contains')
    id_contains_nocase = sgqlc.types.Field(String, graphql_name='id_contains_nocase')
    id_not_contains = sgqlc.types.Field(String, graphql_name='id_not_contains')
    id_not_contains_nocase = sgqlc.types.Field(String, graphql_name='id_not_contains_nocase')
    id_starts_with = sgqlc.types.Field(String, graphql_name='id_starts_with')
    id_starts_with_nocase = sgqlc.types.Field(String, graphql_name='id_starts_with_nocase')
    id_not_starts_with = sgqlc.types.Field(String, graphql_name='id_not_starts_with')
    id_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='id_not_starts_with_nocase')
    id_ends_with = sgqlc.types.Field(String, graphql_name='id_ends_with')
    id_ends_with_nocase = sgqlc.types.Field(String, graphql_name='id_ends_with_nocase')
    id_not_ends_with = sgqlc.types.Field(String, graphql_name='id_not_ends_with')
    id_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='id_not_ends_with_nocase')
    pooltx = sgqlc.types.Field(String, graphql_name='pooltx')
    pooltx_not = sgqlc.types.Field(String, graphql_name='pooltx_not')
    pooltx_gt = sgqlc.types.Field(String, graphql_name='pooltx_gt')
    pooltx_lt = sgqlc.types.Field(String, graphql_name='pooltx_lt')
    pooltx_gte = sgqlc.types.Field(String, graphql_name='pooltx_gte')
    pooltx_lte = sgqlc.types.Field(String, graphql_name='pooltx_lte')
    pooltx_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='pooltx_in')
    pooltx_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='pooltx_not_in')
    pooltx_contains = sgqlc.types.Field(String, graphql_name='pooltx_contains')
    pooltx_contains_nocase = sgqlc.types.Field(String, graphql_name='pooltx_contains_nocase')
    pooltx_not_contains = sgqlc.types.Field(String, graphql_name='pooltx_not_contains')
    pooltx_not_contains_nocase = sgqlc.types.Field(String, graphql_name='pooltx_not_contains_nocase')
    pooltx_starts_with = sgqlc.types.Field(String, graphql_name='pooltx_starts_with')
    pooltx_starts_with_nocase = sgqlc.types.Field(String, graphql_name='pooltx_starts_with_nocase')
    pooltx_not_starts_with = sgqlc.types.Field(String, graphql_name='pooltx_not_starts_with')
    pooltx_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='pooltx_not_starts_with_nocase')
    pooltx_ends_with = sgqlc.types.Field(String, graphql_name='pooltx_ends_with')
    pooltx_ends_with_nocase = sgqlc.types.Field(String, graphql_name='pooltx_ends_with_nocase')
    pooltx_not_ends_with = sgqlc.types.Field(String, graphql_name='pooltx_not_ends_with')
    pooltx_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='pooltx_not_ends_with_nocase')
    pooltx_ = sgqlc.types.Field('PoolTx_filter', graphql_name='pooltx_')
    nullifier = sgqlc.types.Field(BigInt, graphql_name='nullifier')
    nullifier_not = sgqlc.types.Field(BigInt, graphql_name='nullifier_not')
    nullifier_gt = sgqlc.types.Field(BigInt, graphql_name='nullifier_gt')
    nullifier_lt = sgqlc.types.Field(BigInt, graphql_name='nullifier_lt')
    nullifier_gte = sgqlc.types.Field(BigInt, graphql_name='nullifier_gte')
    nullifier_lte = sgqlc.types.Field(BigInt, graphql_name='nullifier_lte')
    nullifier_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='nullifier_in')
    nullifier_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='nullifier_not_in')
    index_ref = sgqlc.types.Field(BigInt, graphql_name='index_ref')
    index_ref_not = sgqlc.types.Field(BigInt, graphql_name='index_ref_not')
    index_ref_gt = sgqlc.types.Field(BigInt, graphql_name='index_ref_gt')
    index_ref_lt = sgqlc.types.Field(BigInt, graphql_name='index_ref_lt')
    index_ref_gte = sgqlc.types.Field(BigInt, graphql_name='index_ref_gte')
    index_ref_lte = sgqlc.types.Field(BigInt, graphql_name='index_ref_lte')
    index_ref_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='index_ref_in')
    index_ref_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='index_ref_not_in')
    token_amount = sgqlc.types.Field(BigInt, graphql_name='token_amount')
    token_amount_not = sgqlc.types.Field(BigInt, graphql_name='token_amount_not')
    token_amount_gt = sgqlc.types.Field(BigInt, graphql_name='token_amount_gt')
    token_amount_lt = sgqlc.types.Field(BigInt, graphql_name='token_amount_lt')
    token_amount_gte = sgqlc.types.Field(BigInt, graphql_name='token_amount_gte')
    token_amount_lte = sgqlc.types.Field(BigInt, graphql_name='token_amount_lte')
    token_amount_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='token_amount_in')
    token_amount_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='token_amount_not_in')
    fee = sgqlc.types.Field(BigInt, graphql_name='fee')
    fee_not = sgqlc.types.Field(BigInt, graphql_name='fee_not')
    fee_gt = sgqlc.types.Field(BigInt, graphql_name='fee_gt')
    fee_lt = sgqlc.types.Field(BigInt, graphql_name='fee_lt')
    fee_gte = sgqlc.types.Field(BigInt, graphql_name='fee_gte')
    fee_lte = sgqlc.types.Field(BigInt, graphql_name='fee_lte')
    fee_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='fee_in')
    fee_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='fee_not_in')
    permit_deadline = sgqlc.types.Field(BigInt, graphql_name='permit_deadline')
    permit_deadline_not = sgqlc.types.Field(BigInt, graphql_name='permit_deadline_not')
    permit_deadline_gt = sgqlc.types.Field(BigInt, graphql_name='permit_deadline_gt')
    permit_deadline_lt = sgqlc.types.Field(BigInt, graphql_name='permit_deadline_lt')
    permit_deadline_gte = sgqlc.types.Field(BigInt, graphql_name='permit_deadline_gte')
    permit_deadline_lte = sgqlc.types.Field(BigInt, graphql_name='permit_deadline_lte')
    permit_deadline_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='permit_deadline_in')
    permit_deadline_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='permit_deadline_not_in')
    permit_holder = sgqlc.types.Field(Bytes, graphql_name='permit_holder')
    permit_holder_not = sgqlc.types.Field(Bytes, graphql_name='permit_holder_not')
    permit_holder_gt = sgqlc.types.Field(Bytes, graphql_name='permit_holder_gt')
    permit_holder_lt = sgqlc.types.Field(Bytes, graphql_name='permit_holder_lt')
    permit_holder_gte = sgqlc.types.Field(Bytes, graphql_name='permit_holder_gte')
    permit_holder_lte = sgqlc.types.Field(Bytes, graphql_name='permit_holder_lte')
    permit_holder_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='permit_holder_in')
    permit_holder_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='permit_holder_not_in')
    permit_holder_contains = sgqlc.types.Field(Bytes, graphql_name='permit_holder_contains')
    permit_holder_not_contains = sgqlc.types.Field(Bytes, graphql_name='permit_holder_not_contains')
    sig = sgqlc.types.Field(Bytes, graphql_name='sig')
    sig_not = sgqlc.types.Field(Bytes, graphql_name='sig_not')
    sig_gt = sgqlc.types.Field(Bytes, graphql_name='sig_gt')
    sig_lt = sgqlc.types.Field(Bytes, graphql_name='sig_lt')
    sig_gte = sgqlc.types.Field(Bytes, graphql_name='sig_gte')
    sig_lte = sgqlc.types.Field(Bytes, graphql_name='sig_lte')
    sig_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='sig_in')
    sig_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='sig_not_in')
    sig_contains = sgqlc.types.Field(Bytes, graphql_name='sig_contains')
    sig_not_contains = sgqlc.types.Field(Bytes, graphql_name='sig_not_contains')
    _change_block = sgqlc.types.Field(BlockChangedFilter, graphql_name='_change_block')
    and_ = sgqlc.types.Field(sgqlc.types.list_of('PermittableDepositOperation_filter'), graphql_name='and')
    or_ = sgqlc.types.Field(sgqlc.types.list_of('PermittableDepositOperation_filter'), graphql_name='or')


class PoolTx_filter(sgqlc.types.Input):
    __schema__ = zkbob_pool_schema
    __field_names__ = ('id', 'id_not', 'id_gt', 'id_lt', 'id_gte', 'id_lte', 'id_in', 'id_not_in', 'id_contains', 'id_contains_nocase', 'id_not_contains', 'id_not_contains_nocase', 'id_starts_with', 'id_starts_with_nocase', 'id_not_starts_with', 'id_not_starts_with_nocase', 'id_ends_with', 'id_ends_with_nocase', 'id_not_ends_with', 'id_not_ends_with_nocase', 'index', 'index_not', 'index_gt', 'index_lt', 'index_gte', 'index_lte', 'index_in', 'index_not_in', 'tx', 'tx_not', 'tx_gt', 'tx_lt', 'tx_gte', 'tx_lte', 'tx_in', 'tx_not_in', 'tx_contains', 'tx_not_contains', 'ts', 'ts_not', 'ts_gt', 'ts_lt', 'ts_gte', 'ts_lte', 'ts_in', 'ts_not_in', 'all_messages_hash', 'all_messages_hash_not', 'all_messages_hash_gt', 'all_messages_hash_lt', 'all_messages_hash_gte', 'all_messages_hash_lte', 'all_messages_hash_in', 'all_messages_hash_not_in', 'all_messages_hash_contains', 'all_messages_hash_not_contains', 'type', 'type_not', 'type_gt', 'type_lt', 'type_gte', 'type_lte', 'type_in', 'type_not_in', 'message', 'message_not', 'message_gt', 'message_lt', 'message_gte', 'message_lte', 'message_in', 'message_not_in', 'message_contains', 'message_not_contains', 'gas_used', 'gas_used_not', 'gas_used_gt', 'gas_used_lt', 'gas_used_gte', 'gas_used_lte', 'gas_used_in', 'gas_used_not_in', 'zk', 'zk_not', 'zk_gt', 'zk_lt', 'zk_gte', 'zk_lte', 'zk_in', 'zk_not_in', 'zk_contains', 'zk_contains_nocase', 'zk_not_contains', 'zk_not_contains_nocase', 'zk_starts_with', 'zk_starts_with_nocase', 'zk_not_starts_with', 'zk_not_starts_with_nocase', 'zk_ends_with', 'zk_ends_with_nocase', 'zk_not_ends_with', 'zk_not_ends_with_nocase', 'zk_', 'operation', 'operation_not', 'operation_gt', 'operation_lt', 'operation_gte', 'operation_lte', 'operation_in', 'operation_not_in', 'operation_contains', 'operation_contains_nocase', 'operation_not_contains', 'operation_not_contains_nocase', 'operation_starts_with', 'operation_starts_with_nocase', 'operation_not_starts_with', 'operation_not_starts_with_nocase', 'operation_ends_with', 'operation_ends_with_nocase', 'operation_not_ends_with', 'operation_not_ends_with_nocase', 'operation_', 'calldata', 'calldata_not', 'calldata_gt', 'calldata_lt', 'calldata_gte', 'calldata_lte', 'calldata_in', 'calldata_not_in', 'calldata_contains', 'calldata_not_contains', '_change_block', 'and_', 'or_')
    id = sgqlc.types.Field(String, graphql_name='id')
    id_not = sgqlc.types.Field(String, graphql_name='id_not')
    id_gt = sgqlc.types.Field(String, graphql_name='id_gt')
    id_lt = sgqlc.types.Field(String, graphql_name='id_lt')
    id_gte = sgqlc.types.Field(String, graphql_name='id_gte')
    id_lte = sgqlc.types.Field(String, graphql_name='id_lte')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='id_not_in')
    id_contains = sgqlc.types.Field(String, graphql_name='id_contains')
    id_contains_nocase = sgqlc.types.Field(String, graphql_name='id_contains_nocase')
    id_not_contains = sgqlc.types.Field(String, graphql_name='id_not_contains')
    id_not_contains_nocase = sgqlc.types.Field(String, graphql_name='id_not_contains_nocase')
    id_starts_with = sgqlc.types.Field(String, graphql_name='id_starts_with')
    id_starts_with_nocase = sgqlc.types.Field(String, graphql_name='id_starts_with_nocase')
    id_not_starts_with = sgqlc.types.Field(String, graphql_name='id_not_starts_with')
    id_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='id_not_starts_with_nocase')
    id_ends_with = sgqlc.types.Field(String, graphql_name='id_ends_with')
    id_ends_with_nocase = sgqlc.types.Field(String, graphql_name='id_ends_with_nocase')
    id_not_ends_with = sgqlc.types.Field(String, graphql_name='id_not_ends_with')
    id_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='id_not_ends_with_nocase')
    index = sgqlc.types.Field(BigInt, graphql_name='index')
    index_not = sgqlc.types.Field(BigInt, graphql_name='index_not')
    index_gt = sgqlc.types.Field(BigInt, graphql_name='index_gt')
    index_lt = sgqlc.types.Field(BigInt, graphql_name='index_lt')
    index_gte = sgqlc.types.Field(BigInt, graphql_name='index_gte')
    index_lte = sgqlc.types.Field(BigInt, graphql_name='index_lte')
    index_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='index_in')
    index_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='index_not_in')
    tx = sgqlc.types.Field(Bytes, graphql_name='tx')
    tx_not = sgqlc.types.Field(Bytes, graphql_name='tx_not')
    tx_gt = sgqlc.types.Field(Bytes, graphql_name='tx_gt')
    tx_lt = sgqlc.types.Field(Bytes, graphql_name='tx_lt')
    tx_gte = sgqlc.types.Field(Bytes, graphql_name='tx_gte')
    tx_lte = sgqlc.types.Field(Bytes, graphql_name='tx_lte')
    tx_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='tx_in')
    tx_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='tx_not_in')
    tx_contains = sgqlc.types.Field(Bytes, graphql_name='tx_contains')
    tx_not_contains = sgqlc.types.Field(Bytes, graphql_name='tx_not_contains')
    ts = sgqlc.types.Field(BigInt, graphql_name='ts')
    ts_not = sgqlc.types.Field(BigInt, graphql_name='ts_not')
    ts_gt = sgqlc.types.Field(BigInt, graphql_name='ts_gt')
    ts_lt = sgqlc.types.Field(BigInt, graphql_name='ts_lt')
    ts_gte = sgqlc.types.Field(BigInt, graphql_name='ts_gte')
    ts_lte = sgqlc.types.Field(BigInt, graphql_name='ts_lte')
    ts_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='ts_in')
    ts_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='ts_not_in')
    all_messages_hash = sgqlc.types.Field(Bytes, graphql_name='all_messages_hash')
    all_messages_hash_not = sgqlc.types.Field(Bytes, graphql_name='all_messages_hash_not')
    all_messages_hash_gt = sgqlc.types.Field(Bytes, graphql_name='all_messages_hash_gt')
    all_messages_hash_lt = sgqlc.types.Field(Bytes, graphql_name='all_messages_hash_lt')
    all_messages_hash_gte = sgqlc.types.Field(Bytes, graphql_name='all_messages_hash_gte')
    all_messages_hash_lte = sgqlc.types.Field(Bytes, graphql_name='all_messages_hash_lte')
    all_messages_hash_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='all_messages_hash_in')
    all_messages_hash_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='all_messages_hash_not_in')
    all_messages_hash_contains = sgqlc.types.Field(Bytes, graphql_name='all_messages_hash_contains')
    all_messages_hash_not_contains = sgqlc.types.Field(Bytes, graphql_name='all_messages_hash_not_contains')
    type = sgqlc.types.Field(Int, graphql_name='type')
    type_not = sgqlc.types.Field(Int, graphql_name='type_not')
    type_gt = sgqlc.types.Field(Int, graphql_name='type_gt')
    type_lt = sgqlc.types.Field(Int, graphql_name='type_lt')
    type_gte = sgqlc.types.Field(Int, graphql_name='type_gte')
    type_lte = sgqlc.types.Field(Int, graphql_name='type_lte')
    type_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='type_in')
    type_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='type_not_in')
    message = sgqlc.types.Field(Bytes, graphql_name='message')
    message_not = sgqlc.types.Field(Bytes, graphql_name='message_not')
    message_gt = sgqlc.types.Field(Bytes, graphql_name='message_gt')
    message_lt = sgqlc.types.Field(Bytes, graphql_name='message_lt')
    message_gte = sgqlc.types.Field(Bytes, graphql_name='message_gte')
    message_lte = sgqlc.types.Field(Bytes, graphql_name='message_lte')
    message_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='message_in')
    message_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='message_not_in')
    message_contains = sgqlc.types.Field(Bytes, graphql_name='message_contains')
    message_not_contains = sgqlc.types.Field(Bytes, graphql_name='message_not_contains')
    gas_used = sgqlc.types.Field(Int, graphql_name='gas_used')
    gas_used_not = sgqlc.types.Field(Int, graphql_name='gas_used_not')
    gas_used_gt = sgqlc.types.Field(Int, graphql_name='gas_used_gt')
    gas_used_lt = sgqlc.types.Field(Int, graphql_name='gas_used_lt')
    gas_used_gte = sgqlc.types.Field(Int, graphql_name='gas_used_gte')
    gas_used_lte = sgqlc.types.Field(Int, graphql_name='gas_used_lte')
    gas_used_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='gas_used_in')
    gas_used_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='gas_used_not_in')
    zk = sgqlc.types.Field(String, graphql_name='zk')
    zk_not = sgqlc.types.Field(String, graphql_name='zk_not')
    zk_gt = sgqlc.types.Field(String, graphql_name='zk_gt')
    zk_lt = sgqlc.types.Field(String, graphql_name='zk_lt')
    zk_gte = sgqlc.types.Field(String, graphql_name='zk_gte')
    zk_lte = sgqlc.types.Field(String, graphql_name='zk_lte')
    zk_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='zk_in')
    zk_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='zk_not_in')
    zk_contains = sgqlc.types.Field(String, graphql_name='zk_contains')
    zk_contains_nocase = sgqlc.types.Field(String, graphql_name='zk_contains_nocase')
    zk_not_contains = sgqlc.types.Field(String, graphql_name='zk_not_contains')
    zk_not_contains_nocase = sgqlc.types.Field(String, graphql_name='zk_not_contains_nocase')
    zk_starts_with = sgqlc.types.Field(String, graphql_name='zk_starts_with')
    zk_starts_with_nocase = sgqlc.types.Field(String, graphql_name='zk_starts_with_nocase')
    zk_not_starts_with = sgqlc.types.Field(String, graphql_name='zk_not_starts_with')
    zk_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='zk_not_starts_with_nocase')
    zk_ends_with = sgqlc.types.Field(String, graphql_name='zk_ends_with')
    zk_ends_with_nocase = sgqlc.types.Field(String, graphql_name='zk_ends_with_nocase')
    zk_not_ends_with = sgqlc.types.Field(String, graphql_name='zk_not_ends_with')
    zk_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='zk_not_ends_with_nocase')
    zk_ = sgqlc.types.Field('ZkCommon_filter', graphql_name='zk_')
    operation = sgqlc.types.Field(String, graphql_name='operation')
    operation_not = sgqlc.types.Field(String, graphql_name='operation_not')
    operation_gt = sgqlc.types.Field(String, graphql_name='operation_gt')
    operation_lt = sgqlc.types.Field(String, graphql_name='operation_lt')
    operation_gte = sgqlc.types.Field(String, graphql_name='operation_gte')
    operation_lte = sgqlc.types.Field(String, graphql_name='operation_lte')
    operation_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='operation_in')
    operation_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='operation_not_in')
    operation_contains = sgqlc.types.Field(String, graphql_name='operation_contains')
    operation_contains_nocase = sgqlc.types.Field(String, graphql_name='operation_contains_nocase')
    operation_not_contains = sgqlc.types.Field(String, graphql_name='operation_not_contains')
    operation_not_contains_nocase = sgqlc.types.Field(String, graphql_name='operation_not_contains_nocase')
    operation_starts_with = sgqlc.types.Field(String, graphql_name='operation_starts_with')
    operation_starts_with_nocase = sgqlc.types.Field(String, graphql_name='operation_starts_with_nocase')
    operation_not_starts_with = sgqlc.types.Field(String, graphql_name='operation_not_starts_with')
    operation_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='operation_not_starts_with_nocase')
    operation_ends_with = sgqlc.types.Field(String, graphql_name='operation_ends_with')
    operation_ends_with_nocase = sgqlc.types.Field(String, graphql_name='operation_ends_with_nocase')
    operation_not_ends_with = sgqlc.types.Field(String, graphql_name='operation_not_ends_with')
    operation_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='operation_not_ends_with_nocase')
    operation_ = sgqlc.types.Field(Operation_filter, graphql_name='operation_')
    calldata = sgqlc.types.Field(Bytes, graphql_name='calldata')
    calldata_not = sgqlc.types.Field(Bytes, graphql_name='calldata_not')
    calldata_gt = sgqlc.types.Field(Bytes, graphql_name='calldata_gt')
    calldata_lt = sgqlc.types.Field(Bytes, graphql_name='calldata_lt')
    calldata_gte = sgqlc.types.Field(Bytes, graphql_name='calldata_gte')
    calldata_lte = sgqlc.types.Field(Bytes, graphql_name='calldata_lte')
    calldata_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='calldata_in')
    calldata_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='calldata_not_in')
    calldata_contains = sgqlc.types.Field(Bytes, graphql_name='calldata_contains')
    calldata_not_contains = sgqlc.types.Field(Bytes, graphql_name='calldata_not_contains')
    _change_block = sgqlc.types.Field(BlockChangedFilter, graphql_name='_change_block')
    and_ = sgqlc.types.Field(sgqlc.types.list_of('PoolTx_filter'), graphql_name='and')
    or_ = sgqlc.types.Field(sgqlc.types.list_of('PoolTx_filter'), graphql_name='or')


class TransferOperation_filter(sgqlc.types.Input):
    __schema__ = zkbob_pool_schema
    __field_names__ = ('id', 'id_not', 'id_gt', 'id_lt', 'id_gte', 'id_lte', 'id_in', 'id_not_in', 'id_contains', 'id_contains_nocase', 'id_not_contains', 'id_not_contains_nocase', 'id_starts_with', 'id_starts_with_nocase', 'id_not_starts_with', 'id_not_starts_with_nocase', 'id_ends_with', 'id_ends_with_nocase', 'id_not_ends_with', 'id_not_ends_with_nocase', 'pooltx', 'pooltx_not', 'pooltx_gt', 'pooltx_lt', 'pooltx_gte', 'pooltx_lte', 'pooltx_in', 'pooltx_not_in', 'pooltx_contains', 'pooltx_contains_nocase', 'pooltx_not_contains', 'pooltx_not_contains_nocase', 'pooltx_starts_with', 'pooltx_starts_with_nocase', 'pooltx_not_starts_with', 'pooltx_not_starts_with_nocase', 'pooltx_ends_with', 'pooltx_ends_with_nocase', 'pooltx_not_ends_with', 'pooltx_not_ends_with_nocase', 'pooltx_', 'nullifier', 'nullifier_not', 'nullifier_gt', 'nullifier_lt', 'nullifier_gte', 'nullifier_lte', 'nullifier_in', 'nullifier_not_in', 'index_ref', 'index_ref_not', 'index_ref_gt', 'index_ref_lt', 'index_ref_gte', 'index_ref_lte', 'index_ref_in', 'index_ref_not_in', 'fee', 'fee_not', 'fee_gt', 'fee_lt', 'fee_gte', 'fee_lte', 'fee_in', 'fee_not_in', '_change_block', 'and_', 'or_')
    id = sgqlc.types.Field(String, graphql_name='id')
    id_not = sgqlc.types.Field(String, graphql_name='id_not')
    id_gt = sgqlc.types.Field(String, graphql_name='id_gt')
    id_lt = sgqlc.types.Field(String, graphql_name='id_lt')
    id_gte = sgqlc.types.Field(String, graphql_name='id_gte')
    id_lte = sgqlc.types.Field(String, graphql_name='id_lte')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='id_not_in')
    id_contains = sgqlc.types.Field(String, graphql_name='id_contains')
    id_contains_nocase = sgqlc.types.Field(String, graphql_name='id_contains_nocase')
    id_not_contains = sgqlc.types.Field(String, graphql_name='id_not_contains')
    id_not_contains_nocase = sgqlc.types.Field(String, graphql_name='id_not_contains_nocase')
    id_starts_with = sgqlc.types.Field(String, graphql_name='id_starts_with')
    id_starts_with_nocase = sgqlc.types.Field(String, graphql_name='id_starts_with_nocase')
    id_not_starts_with = sgqlc.types.Field(String, graphql_name='id_not_starts_with')
    id_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='id_not_starts_with_nocase')
    id_ends_with = sgqlc.types.Field(String, graphql_name='id_ends_with')
    id_ends_with_nocase = sgqlc.types.Field(String, graphql_name='id_ends_with_nocase')
    id_not_ends_with = sgqlc.types.Field(String, graphql_name='id_not_ends_with')
    id_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='id_not_ends_with_nocase')
    pooltx = sgqlc.types.Field(String, graphql_name='pooltx')
    pooltx_not = sgqlc.types.Field(String, graphql_name='pooltx_not')
    pooltx_gt = sgqlc.types.Field(String, graphql_name='pooltx_gt')
    pooltx_lt = sgqlc.types.Field(String, graphql_name='pooltx_lt')
    pooltx_gte = sgqlc.types.Field(String, graphql_name='pooltx_gte')
    pooltx_lte = sgqlc.types.Field(String, graphql_name='pooltx_lte')
    pooltx_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='pooltx_in')
    pooltx_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='pooltx_not_in')
    pooltx_contains = sgqlc.types.Field(String, graphql_name='pooltx_contains')
    pooltx_contains_nocase = sgqlc.types.Field(String, graphql_name='pooltx_contains_nocase')
    pooltx_not_contains = sgqlc.types.Field(String, graphql_name='pooltx_not_contains')
    pooltx_not_contains_nocase = sgqlc.types.Field(String, graphql_name='pooltx_not_contains_nocase')
    pooltx_starts_with = sgqlc.types.Field(String, graphql_name='pooltx_starts_with')
    pooltx_starts_with_nocase = sgqlc.types.Field(String, graphql_name='pooltx_starts_with_nocase')
    pooltx_not_starts_with = sgqlc.types.Field(String, graphql_name='pooltx_not_starts_with')
    pooltx_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='pooltx_not_starts_with_nocase')
    pooltx_ends_with = sgqlc.types.Field(String, graphql_name='pooltx_ends_with')
    pooltx_ends_with_nocase = sgqlc.types.Field(String, graphql_name='pooltx_ends_with_nocase')
    pooltx_not_ends_with = sgqlc.types.Field(String, graphql_name='pooltx_not_ends_with')
    pooltx_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='pooltx_not_ends_with_nocase')
    pooltx_ = sgqlc.types.Field(PoolTx_filter, graphql_name='pooltx_')
    nullifier = sgqlc.types.Field(BigInt, graphql_name='nullifier')
    nullifier_not = sgqlc.types.Field(BigInt, graphql_name='nullifier_not')
    nullifier_gt = sgqlc.types.Field(BigInt, graphql_name='nullifier_gt')
    nullifier_lt = sgqlc.types.Field(BigInt, graphql_name='nullifier_lt')
    nullifier_gte = sgqlc.types.Field(BigInt, graphql_name='nullifier_gte')
    nullifier_lte = sgqlc.types.Field(BigInt, graphql_name='nullifier_lte')
    nullifier_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='nullifier_in')
    nullifier_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='nullifier_not_in')
    index_ref = sgqlc.types.Field(BigInt, graphql_name='index_ref')
    index_ref_not = sgqlc.types.Field(BigInt, graphql_name='index_ref_not')
    index_ref_gt = sgqlc.types.Field(BigInt, graphql_name='index_ref_gt')
    index_ref_lt = sgqlc.types.Field(BigInt, graphql_name='index_ref_lt')
    index_ref_gte = sgqlc.types.Field(BigInt, graphql_name='index_ref_gte')
    index_ref_lte = sgqlc.types.Field(BigInt, graphql_name='index_ref_lte')
    index_ref_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='index_ref_in')
    index_ref_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='index_ref_not_in')
    fee = sgqlc.types.Field(BigInt, graphql_name='fee')
    fee_not = sgqlc.types.Field(BigInt, graphql_name='fee_not')
    fee_gt = sgqlc.types.Field(BigInt, graphql_name='fee_gt')
    fee_lt = sgqlc.types.Field(BigInt, graphql_name='fee_lt')
    fee_gte = sgqlc.types.Field(BigInt, graphql_name='fee_gte')
    fee_lte = sgqlc.types.Field(BigInt, graphql_name='fee_lte')
    fee_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='fee_in')
    fee_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='fee_not_in')
    _change_block = sgqlc.types.Field(BlockChangedFilter, graphql_name='_change_block')
    and_ = sgqlc.types.Field(sgqlc.types.list_of('TransferOperation_filter'), graphql_name='and')
    or_ = sgqlc.types.Field(sgqlc.types.list_of('TransferOperation_filter'), graphql_name='or')


class WithdrawalOperation_filter(sgqlc.types.Input):
    __schema__ = zkbob_pool_schema
    __field_names__ = ('id', 'id_not', 'id_gt', 'id_lt', 'id_gte', 'id_lte', 'id_in', 'id_not_in', 'id_contains', 'id_contains_nocase', 'id_not_contains', 'id_not_contains_nocase', 'id_starts_with', 'id_starts_with_nocase', 'id_not_starts_with', 'id_not_starts_with_nocase', 'id_ends_with', 'id_ends_with_nocase', 'id_not_ends_with', 'id_not_ends_with_nocase', 'pooltx', 'pooltx_not', 'pooltx_gt', 'pooltx_lt', 'pooltx_gte', 'pooltx_lte', 'pooltx_in', 'pooltx_not_in', 'pooltx_contains', 'pooltx_contains_nocase', 'pooltx_not_contains', 'pooltx_not_contains_nocase', 'pooltx_starts_with', 'pooltx_starts_with_nocase', 'pooltx_not_starts_with', 'pooltx_not_starts_with_nocase', 'pooltx_ends_with', 'pooltx_ends_with_nocase', 'pooltx_not_ends_with', 'pooltx_not_ends_with_nocase', 'pooltx_', 'nullifier', 'nullifier_not', 'nullifier_gt', 'nullifier_lt', 'nullifier_gte', 'nullifier_lte', 'nullifier_in', 'nullifier_not_in', 'index_ref', 'index_ref_not', 'index_ref_gt', 'index_ref_lt', 'index_ref_gte', 'index_ref_lte', 'index_ref_in', 'index_ref_not_in', 'energy_amount', 'energy_amount_not', 'energy_amount_gt', 'energy_amount_lt', 'energy_amount_gte', 'energy_amount_lte', 'energy_amount_in', 'energy_amount_not_in', 'token_amount', 'token_amount_not', 'token_amount_gt', 'token_amount_lt', 'token_amount_gte', 'token_amount_lte', 'token_amount_in', 'token_amount_not_in', 'fee', 'fee_not', 'fee_gt', 'fee_lt', 'fee_gte', 'fee_lte', 'fee_in', 'fee_not_in', 'native_amount', 'native_amount_not', 'native_amount_gt', 'native_amount_lt', 'native_amount_gte', 'native_amount_lte', 'native_amount_in', 'native_amount_not_in', 'receiver', 'receiver_not', 'receiver_gt', 'receiver_lt', 'receiver_gte', 'receiver_lte', 'receiver_in', 'receiver_not_in', 'receiver_contains', 'receiver_not_contains', '_change_block', 'and_', 'or_')
    id = sgqlc.types.Field(String, graphql_name='id')
    id_not = sgqlc.types.Field(String, graphql_name='id_not')
    id_gt = sgqlc.types.Field(String, graphql_name='id_gt')
    id_lt = sgqlc.types.Field(String, graphql_name='id_lt')
    id_gte = sgqlc.types.Field(String, graphql_name='id_gte')
    id_lte = sgqlc.types.Field(String, graphql_name='id_lte')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='id_not_in')
    id_contains = sgqlc.types.Field(String, graphql_name='id_contains')
    id_contains_nocase = sgqlc.types.Field(String, graphql_name='id_contains_nocase')
    id_not_contains = sgqlc.types.Field(String, graphql_name='id_not_contains')
    id_not_contains_nocase = sgqlc.types.Field(String, graphql_name='id_not_contains_nocase')
    id_starts_with = sgqlc.types.Field(String, graphql_name='id_starts_with')
    id_starts_with_nocase = sgqlc.types.Field(String, graphql_name='id_starts_with_nocase')
    id_not_starts_with = sgqlc.types.Field(String, graphql_name='id_not_starts_with')
    id_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='id_not_starts_with_nocase')
    id_ends_with = sgqlc.types.Field(String, graphql_name='id_ends_with')
    id_ends_with_nocase = sgqlc.types.Field(String, graphql_name='id_ends_with_nocase')
    id_not_ends_with = sgqlc.types.Field(String, graphql_name='id_not_ends_with')
    id_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='id_not_ends_with_nocase')
    pooltx = sgqlc.types.Field(String, graphql_name='pooltx')
    pooltx_not = sgqlc.types.Field(String, graphql_name='pooltx_not')
    pooltx_gt = sgqlc.types.Field(String, graphql_name='pooltx_gt')
    pooltx_lt = sgqlc.types.Field(String, graphql_name='pooltx_lt')
    pooltx_gte = sgqlc.types.Field(String, graphql_name='pooltx_gte')
    pooltx_lte = sgqlc.types.Field(String, graphql_name='pooltx_lte')
    pooltx_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='pooltx_in')
    pooltx_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='pooltx_not_in')
    pooltx_contains = sgqlc.types.Field(String, graphql_name='pooltx_contains')
    pooltx_contains_nocase = sgqlc.types.Field(String, graphql_name='pooltx_contains_nocase')
    pooltx_not_contains = sgqlc.types.Field(String, graphql_name='pooltx_not_contains')
    pooltx_not_contains_nocase = sgqlc.types.Field(String, graphql_name='pooltx_not_contains_nocase')
    pooltx_starts_with = sgqlc.types.Field(String, graphql_name='pooltx_starts_with')
    pooltx_starts_with_nocase = sgqlc.types.Field(String, graphql_name='pooltx_starts_with_nocase')
    pooltx_not_starts_with = sgqlc.types.Field(String, graphql_name='pooltx_not_starts_with')
    pooltx_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='pooltx_not_starts_with_nocase')
    pooltx_ends_with = sgqlc.types.Field(String, graphql_name='pooltx_ends_with')
    pooltx_ends_with_nocase = sgqlc.types.Field(String, graphql_name='pooltx_ends_with_nocase')
    pooltx_not_ends_with = sgqlc.types.Field(String, graphql_name='pooltx_not_ends_with')
    pooltx_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='pooltx_not_ends_with_nocase')
    pooltx_ = sgqlc.types.Field(PoolTx_filter, graphql_name='pooltx_')
    nullifier = sgqlc.types.Field(BigInt, graphql_name='nullifier')
    nullifier_not = sgqlc.types.Field(BigInt, graphql_name='nullifier_not')
    nullifier_gt = sgqlc.types.Field(BigInt, graphql_name='nullifier_gt')
    nullifier_lt = sgqlc.types.Field(BigInt, graphql_name='nullifier_lt')
    nullifier_gte = sgqlc.types.Field(BigInt, graphql_name='nullifier_gte')
    nullifier_lte = sgqlc.types.Field(BigInt, graphql_name='nullifier_lte')
    nullifier_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='nullifier_in')
    nullifier_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='nullifier_not_in')
    index_ref = sgqlc.types.Field(BigInt, graphql_name='index_ref')
    index_ref_not = sgqlc.types.Field(BigInt, graphql_name='index_ref_not')
    index_ref_gt = sgqlc.types.Field(BigInt, graphql_name='index_ref_gt')
    index_ref_lt = sgqlc.types.Field(BigInt, graphql_name='index_ref_lt')
    index_ref_gte = sgqlc.types.Field(BigInt, graphql_name='index_ref_gte')
    index_ref_lte = sgqlc.types.Field(BigInt, graphql_name='index_ref_lte')
    index_ref_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='index_ref_in')
    index_ref_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='index_ref_not_in')
    energy_amount = sgqlc.types.Field(BigInt, graphql_name='energy_amount')
    energy_amount_not = sgqlc.types.Field(BigInt, graphql_name='energy_amount_not')
    energy_amount_gt = sgqlc.types.Field(BigInt, graphql_name='energy_amount_gt')
    energy_amount_lt = sgqlc.types.Field(BigInt, graphql_name='energy_amount_lt')
    energy_amount_gte = sgqlc.types.Field(BigInt, graphql_name='energy_amount_gte')
    energy_amount_lte = sgqlc.types.Field(BigInt, graphql_name='energy_amount_lte')
    energy_amount_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='energy_amount_in')
    energy_amount_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='energy_amount_not_in')
    token_amount = sgqlc.types.Field(BigInt, graphql_name='token_amount')
    token_amount_not = sgqlc.types.Field(BigInt, graphql_name='token_amount_not')
    token_amount_gt = sgqlc.types.Field(BigInt, graphql_name='token_amount_gt')
    token_amount_lt = sgqlc.types.Field(BigInt, graphql_name='token_amount_lt')
    token_amount_gte = sgqlc.types.Field(BigInt, graphql_name='token_amount_gte')
    token_amount_lte = sgqlc.types.Field(BigInt, graphql_name='token_amount_lte')
    token_amount_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='token_amount_in')
    token_amount_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='token_amount_not_in')
    fee = sgqlc.types.Field(BigInt, graphql_name='fee')
    fee_not = sgqlc.types.Field(BigInt, graphql_name='fee_not')
    fee_gt = sgqlc.types.Field(BigInt, graphql_name='fee_gt')
    fee_lt = sgqlc.types.Field(BigInt, graphql_name='fee_lt')
    fee_gte = sgqlc.types.Field(BigInt, graphql_name='fee_gte')
    fee_lte = sgqlc.types.Field(BigInt, graphql_name='fee_lte')
    fee_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='fee_in')
    fee_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='fee_not_in')
    native_amount = sgqlc.types.Field(BigInt, graphql_name='native_amount')
    native_amount_not = sgqlc.types.Field(BigInt, graphql_name='native_amount_not')
    native_amount_gt = sgqlc.types.Field(BigInt, graphql_name='native_amount_gt')
    native_amount_lt = sgqlc.types.Field(BigInt, graphql_name='native_amount_lt')
    native_amount_gte = sgqlc.types.Field(BigInt, graphql_name='native_amount_gte')
    native_amount_lte = sgqlc.types.Field(BigInt, graphql_name='native_amount_lte')
    native_amount_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='native_amount_in')
    native_amount_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='native_amount_not_in')
    receiver = sgqlc.types.Field(Bytes, graphql_name='receiver')
    receiver_not = sgqlc.types.Field(Bytes, graphql_name='receiver_not')
    receiver_gt = sgqlc.types.Field(Bytes, graphql_name='receiver_gt')
    receiver_lt = sgqlc.types.Field(Bytes, graphql_name='receiver_lt')
    receiver_gte = sgqlc.types.Field(Bytes, graphql_name='receiver_gte')
    receiver_lte = sgqlc.types.Field(Bytes, graphql_name='receiver_lte')
    receiver_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='receiver_in')
    receiver_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='receiver_not_in')
    receiver_contains = sgqlc.types.Field(Bytes, graphql_name='receiver_contains')
    receiver_not_contains = sgqlc.types.Field(Bytes, graphql_name='receiver_not_contains')
    _change_block = sgqlc.types.Field(BlockChangedFilter, graphql_name='_change_block')
    and_ = sgqlc.types.Field(sgqlc.types.list_of('WithdrawalOperation_filter'), graphql_name='and')
    or_ = sgqlc.types.Field(sgqlc.types.list_of('WithdrawalOperation_filter'), graphql_name='or')


class ZkCommon_filter(sgqlc.types.Input):
    __schema__ = zkbob_pool_schema
    __field_names__ = ('id', 'id_not', 'id_gt', 'id_lt', 'id_gte', 'id_lte', 'id_in', 'id_not_in', 'id_contains', 'id_contains_nocase', 'id_not_contains', 'id_not_contains_nocase', 'id_starts_with', 'id_starts_with_nocase', 'id_not_starts_with', 'id_not_starts_with_nocase', 'id_ends_with', 'id_ends_with_nocase', 'id_not_ends_with', 'id_not_ends_with_nocase', 'pooltx', 'pooltx_not', 'pooltx_gt', 'pooltx_lt', 'pooltx_gte', 'pooltx_lte', 'pooltx_in', 'pooltx_not_in', 'pooltx_contains', 'pooltx_contains_nocase', 'pooltx_not_contains', 'pooltx_not_contains_nocase', 'pooltx_starts_with', 'pooltx_starts_with_nocase', 'pooltx_not_starts_with', 'pooltx_not_starts_with_nocase', 'pooltx_ends_with', 'pooltx_ends_with_nocase', 'pooltx_not_ends_with', 'pooltx_not_ends_with_nocase', 'pooltx_', 'out_commit', 'out_commit_not', 'out_commit_gt', 'out_commit_lt', 'out_commit_gte', 'out_commit_lte', 'out_commit_in', 'out_commit_not_in', 'witness', 'witness_not', 'witness_contains', 'witness_contains_nocase', 'witness_not_contains', 'witness_not_contains_nocase', 'tree_root_after', 'tree_root_after_not', 'tree_root_after_gt', 'tree_root_after_lt', 'tree_root_after_gte', 'tree_root_after_lte', 'tree_root_after_in', 'tree_root_after_not_in', 'tree_proof', 'tree_proof_not', 'tree_proof_contains', 'tree_proof_contains_nocase', 'tree_proof_not_contains', 'tree_proof_not_contains_nocase', '_change_block', 'and_', 'or_')
    id = sgqlc.types.Field(String, graphql_name='id')
    id_not = sgqlc.types.Field(String, graphql_name='id_not')
    id_gt = sgqlc.types.Field(String, graphql_name='id_gt')
    id_lt = sgqlc.types.Field(String, graphql_name='id_lt')
    id_gte = sgqlc.types.Field(String, graphql_name='id_gte')
    id_lte = sgqlc.types.Field(String, graphql_name='id_lte')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='id_not_in')
    id_contains = sgqlc.types.Field(String, graphql_name='id_contains')
    id_contains_nocase = sgqlc.types.Field(String, graphql_name='id_contains_nocase')
    id_not_contains = sgqlc.types.Field(String, graphql_name='id_not_contains')
    id_not_contains_nocase = sgqlc.types.Field(String, graphql_name='id_not_contains_nocase')
    id_starts_with = sgqlc.types.Field(String, graphql_name='id_starts_with')
    id_starts_with_nocase = sgqlc.types.Field(String, graphql_name='id_starts_with_nocase')
    id_not_starts_with = sgqlc.types.Field(String, graphql_name='id_not_starts_with')
    id_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='id_not_starts_with_nocase')
    id_ends_with = sgqlc.types.Field(String, graphql_name='id_ends_with')
    id_ends_with_nocase = sgqlc.types.Field(String, graphql_name='id_ends_with_nocase')
    id_not_ends_with = sgqlc.types.Field(String, graphql_name='id_not_ends_with')
    id_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='id_not_ends_with_nocase')
    pooltx = sgqlc.types.Field(String, graphql_name='pooltx')
    pooltx_not = sgqlc.types.Field(String, graphql_name='pooltx_not')
    pooltx_gt = sgqlc.types.Field(String, graphql_name='pooltx_gt')
    pooltx_lt = sgqlc.types.Field(String, graphql_name='pooltx_lt')
    pooltx_gte = sgqlc.types.Field(String, graphql_name='pooltx_gte')
    pooltx_lte = sgqlc.types.Field(String, graphql_name='pooltx_lte')
    pooltx_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='pooltx_in')
    pooltx_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='pooltx_not_in')
    pooltx_contains = sgqlc.types.Field(String, graphql_name='pooltx_contains')
    pooltx_contains_nocase = sgqlc.types.Field(String, graphql_name='pooltx_contains_nocase')
    pooltx_not_contains = sgqlc.types.Field(String, graphql_name='pooltx_not_contains')
    pooltx_not_contains_nocase = sgqlc.types.Field(String, graphql_name='pooltx_not_contains_nocase')
    pooltx_starts_with = sgqlc.types.Field(String, graphql_name='pooltx_starts_with')
    pooltx_starts_with_nocase = sgqlc.types.Field(String, graphql_name='pooltx_starts_with_nocase')
    pooltx_not_starts_with = sgqlc.types.Field(String, graphql_name='pooltx_not_starts_with')
    pooltx_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='pooltx_not_starts_with_nocase')
    pooltx_ends_with = sgqlc.types.Field(String, graphql_name='pooltx_ends_with')
    pooltx_ends_with_nocase = sgqlc.types.Field(String, graphql_name='pooltx_ends_with_nocase')
    pooltx_not_ends_with = sgqlc.types.Field(String, graphql_name='pooltx_not_ends_with')
    pooltx_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='pooltx_not_ends_with_nocase')
    pooltx_ = sgqlc.types.Field(PoolTx_filter, graphql_name='pooltx_')
    out_commit = sgqlc.types.Field(BigInt, graphql_name='out_commit')
    out_commit_not = sgqlc.types.Field(BigInt, graphql_name='out_commit_not')
    out_commit_gt = sgqlc.types.Field(BigInt, graphql_name='out_commit_gt')
    out_commit_lt = sgqlc.types.Field(BigInt, graphql_name='out_commit_lt')
    out_commit_gte = sgqlc.types.Field(BigInt, graphql_name='out_commit_gte')
    out_commit_lte = sgqlc.types.Field(BigInt, graphql_name='out_commit_lte')
    out_commit_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='out_commit_in')
    out_commit_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='out_commit_not_in')
    witness = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='witness')
    witness_not = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='witness_not')
    witness_contains = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='witness_contains')
    witness_contains_nocase = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='witness_contains_nocase')
    witness_not_contains = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='witness_not_contains')
    witness_not_contains_nocase = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='witness_not_contains_nocase')
    tree_root_after = sgqlc.types.Field(BigInt, graphql_name='tree_root_after')
    tree_root_after_not = sgqlc.types.Field(BigInt, graphql_name='tree_root_after_not')
    tree_root_after_gt = sgqlc.types.Field(BigInt, graphql_name='tree_root_after_gt')
    tree_root_after_lt = sgqlc.types.Field(BigInt, graphql_name='tree_root_after_lt')
    tree_root_after_gte = sgqlc.types.Field(BigInt, graphql_name='tree_root_after_gte')
    tree_root_after_lte = sgqlc.types.Field(BigInt, graphql_name='tree_root_after_lte')
    tree_root_after_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='tree_root_after_in')
    tree_root_after_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='tree_root_after_not_in')
    tree_proof = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='tree_proof')
    tree_proof_not = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='tree_proof_not')
    tree_proof_contains = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='tree_proof_contains')
    tree_proof_contains_nocase = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='tree_proof_contains_nocase')
    tree_proof_not_contains = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='tree_proof_not_contains')
    tree_proof_not_contains_nocase = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='tree_proof_not_contains_nocase')
    _change_block = sgqlc.types.Field(BlockChangedFilter, graphql_name='_change_block')
    and_ = sgqlc.types.Field(sgqlc.types.list_of('ZkCommon_filter'), graphql_name='and')
    or_ = sgqlc.types.Field(sgqlc.types.list_of('ZkCommon_filter'), graphql_name='or')



########################################################################
# Output Objects and Interfaces
########################################################################
class Operation(sgqlc.types.Interface):
    __schema__ = zkbob_pool_schema
    __field_names__ = ('id', 'pooltx')
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')
    pooltx = sgqlc.types.Field(sgqlc.types.non_null('PoolTx'), graphql_name='pooltx')


class DirectDeposit(sgqlc.types.Type):
    __schema__ = zkbob_pool_schema
    __field_names__ = ('id', 'index', 'pending', 'completed', 'refunded', 'sender', 'fallback_user', 'zk_address_diversifier', 'zk_address_pk', 'deposit', 'fee', 'bn_init', 'ts_init', 'tx_init', 'payment', 'bn_closed', 'ts_closed', 'tx_closed')
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')
    index = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='index')
    pending = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='pending')
    completed = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='completed')
    refunded = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='refunded')
    sender = sgqlc.types.Field(sgqlc.types.non_null(Bytes), graphql_name='sender')
    fallback_user = sgqlc.types.Field(sgqlc.types.non_null(Bytes), graphql_name='fallbackUser')
    zk_address_diversifier = sgqlc.types.Field(sgqlc.types.non_null(Bytes), graphql_name='zkAddress_diversifier')
    zk_address_pk = sgqlc.types.Field(sgqlc.types.non_null(Bytes), graphql_name='zkAddress_pk')
    deposit = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='deposit')
    fee = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='fee')
    bn_init = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='bnInit')
    ts_init = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='tsInit')
    tx_init = sgqlc.types.Field(sgqlc.types.non_null(Bytes), graphql_name='txInit')
    payment = sgqlc.types.Field('Payment', graphql_name='payment')
    bn_closed = sgqlc.types.Field(BigInt, graphql_name='bnClosed')
    ts_closed = sgqlc.types.Field(BigInt, graphql_name='tsClosed')
    tx_closed = sgqlc.types.Field(Bytes, graphql_name='txClosed')


class LastSyncBlock(sgqlc.types.Type):
    __schema__ = zkbob_pool_schema
    __field_names__ = ('id', 'block')
    id = sgqlc.types.Field(sgqlc.types.non_null(Bytes), graphql_name='id')
    block = sgqlc.types.Field(BigInt, graphql_name='block')


class Payment(sgqlc.types.Type):
    __schema__ = zkbob_pool_schema
    __field_names__ = ('id', 'sender', 'delegated_deposit', 'token', 'note')
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')
    sender = sgqlc.types.Field(Bytes, graphql_name='sender')
    delegated_deposit = sgqlc.types.Field(sgqlc.types.non_null(DirectDeposit), graphql_name='delegated_deposit')
    token = sgqlc.types.Field(sgqlc.types.non_null(Bytes), graphql_name='token')
    note = sgqlc.types.Field(Bytes, graphql_name='note')


class PoolTx(sgqlc.types.Type):
    __schema__ = zkbob_pool_schema
    __field_names__ = ('id', 'index', 'tx', 'ts', 'all_messages_hash', 'type', 'message', 'gas_used', 'zk', 'operation', 'calldata')
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')
    index = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='index')
    tx = sgqlc.types.Field(sgqlc.types.non_null(Bytes), graphql_name='tx')
    ts = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='ts')
    all_messages_hash = sgqlc.types.Field(sgqlc.types.non_null(Bytes), graphql_name='all_messages_hash')
    type = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='type')
    message = sgqlc.types.Field(sgqlc.types.non_null(Bytes), graphql_name='message')
    gas_used = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='gas_used')
    zk = sgqlc.types.Field(sgqlc.types.non_null('ZkCommon'), graphql_name='zk')
    operation = sgqlc.types.Field(sgqlc.types.non_null(Operation), graphql_name='operation')
    calldata = sgqlc.types.Field(sgqlc.types.non_null(Bytes), graphql_name='calldata')


class Query(sgqlc.types.Type):
    __schema__ = zkbob_pool_schema
    __field_names__ = ('direct_deposit', 'direct_deposits', 'payment', 'payments', 'zk_common', 'zk_commons', 'deposit_operation', 'deposit_operations', 'transfer_operation', 'transfer_operations', 'withdrawal_operation', 'withdrawal_operations', 'permittable_deposit_operation', 'permittable_deposit_operations', 'ddbatch_operation', 'ddbatch_operations', 'pool_tx', 'pool_txes', 'last_sync_block', 'last_sync_blocks', 'operation', 'operations', '_meta')
    direct_deposit = sgqlc.types.Field(DirectDeposit, graphql_name='directDeposit', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    direct_deposits = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(DirectDeposit))), graphql_name='directDeposits', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(DirectDeposit_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(DirectDeposit_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    payment = sgqlc.types.Field(Payment, graphql_name='payment', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    payments = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Payment))), graphql_name='payments', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(Payment_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(Payment_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    zk_common = sgqlc.types.Field('ZkCommon', graphql_name='zkCommon', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    zk_commons = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ZkCommon'))), graphql_name='zkCommons', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(ZkCommon_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(ZkCommon_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    deposit_operation = sgqlc.types.Field('DepositOperation', graphql_name='depositOperation', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    deposit_operations = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('DepositOperation'))), graphql_name='depositOperations', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(DepositOperation_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(DepositOperation_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    transfer_operation = sgqlc.types.Field('TransferOperation', graphql_name='transferOperation', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    transfer_operations = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TransferOperation'))), graphql_name='transferOperations', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(TransferOperation_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(TransferOperation_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    withdrawal_operation = sgqlc.types.Field('WithdrawalOperation', graphql_name='withdrawalOperation', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    withdrawal_operations = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('WithdrawalOperation'))), graphql_name='withdrawalOperations', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(WithdrawalOperation_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(WithdrawalOperation_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    permittable_deposit_operation = sgqlc.types.Field('PermittableDepositOperation', graphql_name='permittableDepositOperation', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    permittable_deposit_operations = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('PermittableDepositOperation'))), graphql_name='permittableDepositOperations', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(PermittableDepositOperation_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(PermittableDepositOperation_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    ddbatch_operation = sgqlc.types.Field('DDBatchOperation', graphql_name='ddbatchOperation', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    ddbatch_operations = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('DDBatchOperation'))), graphql_name='ddbatchOperations', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(DDBatchOperation_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(DDBatchOperation_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    pool_tx = sgqlc.types.Field(PoolTx, graphql_name='poolTx', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    pool_txes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(PoolTx))), graphql_name='poolTxes', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(PoolTx_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(PoolTx_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    last_sync_block = sgqlc.types.Field(LastSyncBlock, graphql_name='lastSyncBlock', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    last_sync_blocks = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(LastSyncBlock))), graphql_name='lastSyncBlocks', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(LastSyncBlock_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(LastSyncBlock_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    operation = sgqlc.types.Field(Operation, graphql_name='operation', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    operations = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Operation))), graphql_name='operations', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(Operation_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(Operation_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    _meta = sgqlc.types.Field('_Meta_', graphql_name='_meta', args=sgqlc.types.ArgDict((
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
))
    )


class Subscription(sgqlc.types.Type):
    __schema__ = zkbob_pool_schema
    __field_names__ = ('direct_deposit', 'direct_deposits', 'payment', 'payments', 'zk_common', 'zk_commons', 'deposit_operation', 'deposit_operations', 'transfer_operation', 'transfer_operations', 'withdrawal_operation', 'withdrawal_operations', 'permittable_deposit_operation', 'permittable_deposit_operations', 'ddbatch_operation', 'ddbatch_operations', 'pool_tx', 'pool_txes', 'last_sync_block', 'last_sync_blocks', 'operation', 'operations', '_meta')
    direct_deposit = sgqlc.types.Field(DirectDeposit, graphql_name='directDeposit', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    direct_deposits = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(DirectDeposit))), graphql_name='directDeposits', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(DirectDeposit_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(DirectDeposit_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    payment = sgqlc.types.Field(Payment, graphql_name='payment', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    payments = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Payment))), graphql_name='payments', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(Payment_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(Payment_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    zk_common = sgqlc.types.Field('ZkCommon', graphql_name='zkCommon', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    zk_commons = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ZkCommon'))), graphql_name='zkCommons', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(ZkCommon_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(ZkCommon_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    deposit_operation = sgqlc.types.Field('DepositOperation', graphql_name='depositOperation', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    deposit_operations = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('DepositOperation'))), graphql_name='depositOperations', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(DepositOperation_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(DepositOperation_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    transfer_operation = sgqlc.types.Field('TransferOperation', graphql_name='transferOperation', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    transfer_operations = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TransferOperation'))), graphql_name='transferOperations', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(TransferOperation_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(TransferOperation_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    withdrawal_operation = sgqlc.types.Field('WithdrawalOperation', graphql_name='withdrawalOperation', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    withdrawal_operations = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('WithdrawalOperation'))), graphql_name='withdrawalOperations', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(WithdrawalOperation_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(WithdrawalOperation_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    permittable_deposit_operation = sgqlc.types.Field('PermittableDepositOperation', graphql_name='permittableDepositOperation', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    permittable_deposit_operations = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('PermittableDepositOperation'))), graphql_name='permittableDepositOperations', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(PermittableDepositOperation_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(PermittableDepositOperation_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    ddbatch_operation = sgqlc.types.Field('DDBatchOperation', graphql_name='ddbatchOperation', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    ddbatch_operations = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('DDBatchOperation'))), graphql_name='ddbatchOperations', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(DDBatchOperation_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(DDBatchOperation_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    pool_tx = sgqlc.types.Field(PoolTx, graphql_name='poolTx', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    pool_txes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(PoolTx))), graphql_name='poolTxes', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(PoolTx_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(PoolTx_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    last_sync_block = sgqlc.types.Field(LastSyncBlock, graphql_name='lastSyncBlock', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    last_sync_blocks = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(LastSyncBlock))), graphql_name='lastSyncBlocks', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(LastSyncBlock_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(LastSyncBlock_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    operation = sgqlc.types.Field(Operation, graphql_name='operation', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    operations = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Operation))), graphql_name='operations', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(Operation_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(Operation_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    _meta = sgqlc.types.Field('_Meta_', graphql_name='_meta', args=sgqlc.types.ArgDict((
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
))
    )


class ZkCommon(sgqlc.types.Type):
    __schema__ = zkbob_pool_schema
    __field_names__ = ('id', 'pooltx', 'out_commit', 'witness', 'tree_root_after', 'tree_proof')
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')
    pooltx = sgqlc.types.Field(sgqlc.types.non_null(PoolTx), graphql_name='pooltx')
    out_commit = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='out_commit')
    witness = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(BigInt))), graphql_name='witness')
    tree_root_after = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='tree_root_after')
    tree_proof = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(BigInt))), graphql_name='tree_proof')


class _Block_(sgqlc.types.Type):
    __schema__ = zkbob_pool_schema
    __field_names__ = ('hash', 'number', 'timestamp')
    hash = sgqlc.types.Field(Bytes, graphql_name='hash')
    number = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='number')
    timestamp = sgqlc.types.Field(Int, graphql_name='timestamp')


class _Meta_(sgqlc.types.Type):
    __schema__ = zkbob_pool_schema
    __field_names__ = ('block', 'deployment', 'has_indexing_errors')
    block = sgqlc.types.Field(sgqlc.types.non_null(_Block_), graphql_name='block')
    deployment = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='deployment')
    has_indexing_errors = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasIndexingErrors')


class DDBatchOperation(sgqlc.types.Type, Operation):
    __schema__ = zkbob_pool_schema
    __field_names__ = ('delegated_deposits',)
    delegated_deposits = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(DirectDeposit))), graphql_name='delegated_deposits', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(DirectDeposit_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(DirectDeposit_filter, graphql_name='where', default=None)),
))
    )


class DepositOperation(sgqlc.types.Type, Operation):
    __schema__ = zkbob_pool_schema
    __field_names__ = ('nullifier', 'index_ref', 'token_amount', 'fee')
    nullifier = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='nullifier')
    index_ref = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='index_ref')
    token_amount = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='token_amount')
    fee = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='fee')


class PermittableDepositOperation(sgqlc.types.Type, Operation):
    __schema__ = zkbob_pool_schema
    __field_names__ = ('nullifier', 'index_ref', 'token_amount', 'fee', 'permit_deadline', 'permit_holder', 'sig')
    nullifier = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='nullifier')
    index_ref = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='index_ref')
    token_amount = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='token_amount')
    fee = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='fee')
    permit_deadline = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='permit_deadline')
    permit_holder = sgqlc.types.Field(sgqlc.types.non_null(Bytes), graphql_name='permit_holder')
    sig = sgqlc.types.Field(sgqlc.types.non_null(Bytes), graphql_name='sig')


class TransferOperation(sgqlc.types.Type, Operation):
    __schema__ = zkbob_pool_schema
    __field_names__ = ('nullifier', 'index_ref', 'fee')
    nullifier = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='nullifier')
    index_ref = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='index_ref')
    fee = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='fee')


class WithdrawalOperation(sgqlc.types.Type, Operation):
    __schema__ = zkbob_pool_schema
    __field_names__ = ('nullifier', 'index_ref', 'energy_amount', 'token_amount', 'fee', 'native_amount', 'receiver')
    nullifier = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='nullifier')
    index_ref = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='index_ref')
    energy_amount = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='energy_amount')
    token_amount = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='token_amount')
    fee = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='fee')
    native_amount = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='native_amount')
    receiver = sgqlc.types.Field(sgqlc.types.non_null(Bytes), graphql_name='receiver')



########################################################################
# Unions
########################################################################

########################################################################
# Schema Entry Points
########################################################################
zkbob_pool_schema.query_type = Query
zkbob_pool_schema.mutation_type = None
zkbob_pool_schema.subscription_type = Subscription

