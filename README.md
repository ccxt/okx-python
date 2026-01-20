# okx-python
Python SDK (sync and async) for Okx cryptocurrency exchange with Rest and WS capabilities.

- You can check the SDK docs here: [SDK](https://docs.ccxt.com/#/exchanges/okx)
- You can check Okx's docs here: [Docs](https://www.google.com/search?q=google+okx+cryptocurrency+exchange+api+docs)
- Github repo: https://github.com/ccxt/okx-python
- Pypi package: https://pypi.org/project/okx-exchange


## Installation

```
pip install okx-exchange
```

## Usage

### Sync

```Python
from okx import OkxSync

def main():
    instance = OkxSync({})
    ob =  instance.fetch_order_book("BTC/USDC")
    print(ob)
    #
    # balance = instance.fetch_balance()
    # order = instance.create_order("BTC/USDC", "limit", "buy", 1, 100000)

main()
```

### Async

```Python
import sys
import asyncio
from okx import OkxAsync

### on Windows, uncomment below:
# if sys.platform == 'win32':
# 	asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

async def main():
    instance = OkxAsync({})
    ob =  await instance.fetch_order_book("BTC/USDC")
    print(ob)
    #
    # balance = await instance.fetch_balance()
    # order = await instance.create_order("BTC/USDC", "limit", "buy", 1, 100000)

    # once you are done with the exchange
    await instance.close()

asyncio.run(main())
```



### Websockets

```Python
import sys
from okx import OkxWs

### on Windows, uncomment below:
# if sys.platform == 'win32':
# 	asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

async def main():
    instance = OkxWs({})
    while True:
        ob = await instance.watch_order_book("BTC/USDC")
        print(ob)
        # orders = await instance.watch_orders("BTC/USDC")

    # once you are done with the exchange
    await instance.close()

asyncio.run(main())
```





#### Raw call

You can also construct custom requests to available "implicit" endpoints

```Python
        request = {
            'type': 'candleSnapshot',
            'req': {
                'coin': coin,
                'interval': tf,
                'startTime': since,
                'endTime': until,
            },
        }
        response = await instance.public_post_info(request)
```


## Available methods

### REST Unified

- `create_convert_trade(self, id: str, fromCode: str, toCode: str, amount: Num = None, params={})`
- `create_expired_option_market(self, symbol: str)`
- `create_market_buy_order_with_cost(self, symbol: str, cost: float, params={})`
- `create_market_sell_order_with_cost(self, symbol: str, cost: float, params={})`
- `create_order_request(self, symbol: str, type: OrderType, side: OrderSide, amount: float, price: Num = None, params={})`
- `create_order(self, symbol: str, type: OrderType, side: OrderSide, amount: float, price: Num = None, params={})`
- `create_orders(self, orders: List[OrderRequest], params={})`
- `fetch_accounts(self, params={})`
- `fetch_all_greeks(self, symbols: Strings = None, params={})`
- `fetch_balance(self, params={})`
- `fetch_borrow_interest(self, code: Str = None, symbol: Str = None, since: Int = None, limit: Int = None, params={})`
- `fetch_borrow_rate_histories(self, codes=None, since: Int = None, limit: Int = None, params={})`
- `fetch_borrow_rate_history(self, code: str, since: Int = None, limit: Int = None, params={})`
- `fetch_canceled_orders(self, symbol: Str = None, since: Int = None, limit: Int = None, params={})`
- `fetch_closed_orders(self, symbol: Str = None, since: Int = None, limit: Int = None, params={})`
- `fetch_convert_currencies(self, params={})`
- `fetch_convert_quote(self, fromCode: str, toCode: str, amount: Num = None, params={})`
- `fetch_convert_trade_history(self, code: Str = None, since: Int = None, limit: Int = None, params={})`
- `fetch_convert_trade(self, id: str, code: Str = None, params={})`
- `fetch_cross_borrow_rate(self, code: str, params={})`
- `fetch_cross_borrow_rates(self, params={})`
- `fetch_currencies(self, params={})`
- `fetch_deposit_address(self, code: str, params={})`
- `fetch_deposit_addresses_by_network(self, code: str, params={})`
- `fetch_deposit_withdraw_fees(self, codes: Strings = None, params={})`
- `fetch_deposit(self, id: str, code: Str = None, params={})`
- `fetch_deposits(self, code: Str = None, since: Int = None, limit: Int = None, params={})`
- `fetch_funding_history(self, symbol: Str = None, since: Int = None, limit: Int = None, params={})`
- `fetch_funding_interval(self, symbol: str, params={})`
- `fetch_funding_rate_history(self, symbol: Str = None, since: Int = None, limit: Int = None, params={})`
- `fetch_funding_rate(self, symbol: str, params={})`
- `fetch_funding_rates(self, symbols: Strings = None, params={})`
- `fetch_greeks(self, symbol: str, params={})`
- `fetch_ledger(self, code: Str = None, since: Int = None, limit: Int = None, params={})`
- `fetch_leverage(self, symbol: str, params={})`
- `fetch_long_short_ratio_history(self, symbol: Str = None, timeframe: Str = None, since: Int = None, limit: Int = None, params={})`
- `fetch_margin_adjustment_history(self, symbol: Str = None, type: Str = None, since: Num = None, limit: Num = None, params={})`
- `fetch_mark_price(self, symbol: str, params={})`
- `fetch_mark_prices(self, symbols: Strings = None, params={})`
- `fetch_market_leverage_tiers(self, symbol: str, params={})`
- `fetch_markets_by_type(self, type, params={})`
- `fetch_markets(self, params={})`
- `fetch_my_trades(self, symbol: Str = None, since: Int = None, limit: Int = None, params={})`
- `fetch_ohlcv(self, symbol: str, timeframe: str = '1m', since: Int = None, limit: Int = None, params={})`
- `fetch_open_interest_history(self, symbol: str, timeframe='1d', since: Int = None, limit: Int = None, params={})`
- `fetch_open_interest(self, symbol: str, params={})`
- `fetch_open_interests(self, symbols: Strings = None, params={})`
- `fetch_open_orders(self, symbol: Str = None, since: Int = None, limit: Int = None, params={})`
- `fetch_option_chain(self, code: str, params={})`
- `fetch_option(self, symbol: str, params={})`
- `fetch_order_book(self, symbol: str, limit: Int = None, params={})`
- `fetch_order_trades(self, id: str, symbol: Str = None, since: Int = None, limit: Int = None, params={})`
- `fetch_order(self, id: str, symbol: Str = None, params={})`
- `fetch_position_mode(self, symbol: Str = None, params={})`
- `fetch_position(self, symbol: str, params={})`
- `fetch_positions_for_symbol(self, symbol: str, params={})`
- `fetch_positions_history(self, symbols: Strings = None, since: Int = None, limit: Int = None, params={})`
- `fetch_positions(self, symbols: Strings = None, params={})`
- `fetch_settlement_history(self, symbol: Str = None, since: Int = None, limit: Int = None, params={})`
- `fetch_status(self, params={})`
- `fetch_ticker(self, symbol: str, params={})`
- `fetch_tickers(self, symbols: Strings = None, params={})`
- `fetch_time(self, params={})`
- `fetch_trades(self, symbol: str, since: Int = None, limit: Int = None, params={})`
- `fetch_trading_fee(self, symbol: str, params={})`
- `fetch_transfer(self, id: str, code: Str = None, params={})`
- `fetch_transfers(self, code: Str = None, since: Int = None, limit: Int = None, params={})`
- `fetch_underlying_assets(self, params={})`
- `fetch_withdrawal(self, id: str, code: Str = None, params={})`
- `fetch_withdrawals(self, code: Str = None, since: Int = None, limit: Int = None, params={})`
- `add_margin(self, symbol: str, amount: float, params={})`
- `borrow_cross_margin(self, code: str, amount: float, params={})`
- `cancel_all_orders_after(self, timeout: Int, params={})`
- `cancel_order(self, id: str, symbol: Str = None, params={})`
- `cancel_orders_for_symbols(self, orders: List[CancellationRequest], params={})`
- `cancel_orders(self, ids: List[str], symbol: Str = None, params={})`
- `close_position(self, symbol: str, side: OrderSide = None, params={})`
- `convert_to_instrument_type(self, type)`
- `describe(self)`
- `edit_order_request(self, id: str, symbol, type, side, amount=None, price=None, params={})`
- `edit_order(self, id: str, symbol: str, type: OrderType, side: OrderSide, amount: Num = None, price: Num = None, params={})`
- `modify_margin_helper(self, symbol: str, amount, type, params={})`
- `nonce(self)`
- `reduce_margin(self, symbol: str, amount: float, params={})`
- `repay_cross_margin(self, code: str, amount, params={})`
- `safe_market(self, marketId: Str = None, market: Market = None, delimiter: Str = None, marketType: Str = None)`
- `set_leverage(self, leverage: int, symbol: Str = None, params={})`
- `set_margin_mode(self, marginMode: str, symbol: Str = None, params={})`
- `set_position_mode(self, hedged: bool, symbol: Str = None, params={})`
- `set_sandbox_mode(self, enable: bool)`
- `transfer(self, code: str, amount: float, fromAccount: str, toAccount: str, params={})`
- `withdraw(self, code: str, amount: float, address: str, tag: Str = None, params={})`

### REST Raw

- `public_get_market_tickers(request)`
- `public_get_market_ticker(request)`
- `public_get_market_books(request)`
- `public_get_market_books_full(request)`
- `public_get_market_candles(request)`
- `public_get_market_history_candles(request)`
- `public_get_market_trades(request)`
- `public_get_market_history_trades(request)`
- `public_get_market_option_instrument_family_trades(request)`
- `public_get_market_platform_24_volume(request)`
- `public_get_market_call_auction_detail(request)`
- `public_get_market_books_sbe(request)`
- `public_get_market_block_tickers(request)`
- `public_get_market_block_ticker(request)`
- `public_get_market_sprd_ticker(request)`
- `public_get_market_sprd_candles(request)`
- `public_get_market_sprd_history_candles(request)`
- `public_get_market_index_tickers(request)`
- `public_get_market_index_candles(request)`
- `public_get_market_history_index_candles(request)`
- `public_get_market_mark_price_candles(request)`
- `public_get_market_history_mark_price_candles(request)`
- `public_get_market_exchange_rate(request)`
- `public_get_market_index_components(request)`
- `public_get_market_open_oracle(request)`
- `public_get_market_books_lite(request)`
- `public_get_public_option_trades(request)`
- `public_get_public_block_trades(request)`
- `public_get_public_instruments(request)`
- `public_get_public_estimated_price(request)`
- `public_get_public_delivery_exercise_history(request)`
- `public_get_public_estimated_settlement_info(request)`
- `public_get_public_settlement_history(request)`
- `public_get_public_funding_rate(request)`
- `public_get_public_funding_rate_history(request)`
- `public_get_public_open_interest(request)`
- `public_get_public_price_limit(request)`
- `public_get_public_opt_summary(request)`
- `public_get_public_discount_rate_interest_free_quota(request)`
- `public_get_public_time(request)`
- `public_get_public_mark_price(request)`
- `public_get_public_position_tiers(request)`
- `public_get_public_interest_rate_loan_quota(request)`
- `public_get_public_underlying(request)`
- `public_get_public_insurance_fund(request)`
- `public_get_public_convert_contract_coin(request)`
- `public_get_public_instrument_tick_bands(request)`
- `public_get_public_premium_history(request)`
- `public_get_public_economic_calendar(request)`
- `public_get_public_market_data_history(request)`
- `public_get_public_vip_interest_rate_loan_quota(request)`
- `public_get_rubik_stat_trading_data_support_coin(request)`
- `public_get_rubik_stat_contracts_open_interest_history(request)`
- `public_get_rubik_stat_taker_volume(request)`
- `public_get_rubik_stat_taker_volume_contract(request)`
- `public_get_rubik_stat_margin_loan_ratio(request)`
- `public_get_rubik_stat_contracts_long_short_account_ratio_contract_top_trader(request)`
- `public_get_rubik_stat_contracts_long_short_account_ratio_contract(request)`
- `public_get_rubik_stat_contracts_long_short_account_ratio(request)`
- `public_get_rubik_stat_contracts_open_interest_volume(request)`
- `public_get_rubik_stat_option_open_interest_volume(request)`
- `public_get_rubik_stat_option_open_interest_volume_ratio(request)`
- `public_get_rubik_stat_option_open_interest_volume_expiry(request)`
- `public_get_rubik_stat_option_open_interest_volume_strike(request)`
- `public_get_rubik_stat_option_taker_block_volume(request)`
- `public_get_system_status(request)`
- `public_get_sprd_spreads(request)`
- `public_get_sprd_books(request)`
- `public_get_sprd_public_trades(request)`
- `public_get_sprd_ticker(request)`
- `public_get_tradingbot_grid_ai_param(request)`
- `public_get_tradingbot_grid_min_investment(request)`
- `public_get_tradingbot_public_rsi_back_testing(request)`
- `public_get_tradingbot_grid_grid_quantity(request)`
- `public_get_asset_exchange_list(request)`
- `public_get_finance_staking_defi_eth_apy_history(request)`
- `public_get_finance_staking_defi_sol_apy_history(request)`
- `public_get_finance_savings_lending_rate_summary(request)`
- `public_get_finance_savings_lending_rate_history(request)`
- `public_get_finance_fixed_loan_lending_offers(request)`
- `public_get_finance_fixed_loan_lending_apy_history(request)`
- `public_get_finance_fixed_loan_pending_lending_volume(request)`
- `public_get_finance_sfp_dcd_products(request)`
- `public_get_copytrading_public_config(request)`
- `public_get_copytrading_public_lead_traders(request)`
- `public_get_copytrading_public_weekly_pnl(request)`
- `public_get_copytrading_public_pnl(request)`
- `public_get_copytrading_public_stats(request)`
- `public_get_copytrading_public_preference_currency(request)`
- `public_get_copytrading_public_current_subpositions(request)`
- `public_get_copytrading_public_subpositions_history(request)`
- `public_get_copytrading_public_copy_traders(request)`
- `public_get_support_announcements(request)`
- `public_get_support_announcements_types(request)`
- `public_post_tradingbot_grid_min_investment(request)`
- `private_get_rfq_counterparties(request)`
- `private_get_rfq_maker_instrument_settings(request)`
- `private_get_rfq_mmp_config(request)`
- `private_get_rfq_rfqs(request)`
- `private_get_rfq_quotes(request)`
- `private_get_rfq_trades(request)`
- `private_get_rfq_public_trades(request)`
- `private_get_sprd_order(request)`
- `private_get_sprd_orders_pending(request)`
- `private_get_sprd_orders_history(request)`
- `private_get_sprd_orders_history_archive(request)`
- `private_get_sprd_trades(request)`
- `private_get_trade_order(request)`
- `private_get_trade_orders_pending(request)`
- `private_get_trade_orders_history(request)`
- `private_get_trade_orders_history_archive(request)`
- `private_get_trade_fills(request)`
- `private_get_trade_fills_history(request)`
- `private_get_trade_fills_archive(request)`
- `private_get_trade_order_algo(request)`
- `private_get_trade_orders_algo_pending(request)`
- `private_get_trade_orders_algo_history(request)`
- `private_get_trade_easy_convert_currency_list(request)`
- `private_get_trade_easy_convert_history(request)`
- `private_get_trade_one_click_repay_currency_list(request)`
- `private_get_trade_one_click_repay_currency_list_v2(request)`
- `private_get_trade_one_click_repay_history(request)`
- `private_get_trade_one_click_repay_history_v2(request)`
- `private_get_trade_account_rate_limit(request)`
- `private_get_asset_currencies(request)`
- `private_get_asset_balances(request)`
- `private_get_asset_non_tradable_assets(request)`
- `private_get_asset_asset_valuation(request)`
- `private_get_asset_transfer_state(request)`
- `private_get_asset_bills(request)`
- `private_get_asset_bills_history(request)`
- `private_get_asset_deposit_lightning(request)`
- `private_get_asset_deposit_address(request)`
- `private_get_asset_deposit_history(request)`
- `private_get_asset_withdrawal_history(request)`
- `private_get_asset_deposit_withdraw_status(request)`
- `private_get_asset_monthly_statement(request)`
- `private_get_asset_convert_currencies(request)`
- `private_get_asset_convert_currency_pair(request)`
- `private_get_asset_convert_history(request)`
- `private_get_account_instruments(request)`
- `private_get_account_balance(request)`
- `private_get_account_positions(request)`
- `private_get_account_positions_history(request)`
- `private_get_account_account_position_risk(request)`
- `private_get_account_bills(request)`
- `private_get_account_bills_archive(request)`
- `private_get_account_bills_history_archive(request)`
- `private_get_account_config(request)`
- `private_get_account_max_size(request)`
- `private_get_account_max_avail_size(request)`
- `private_get_account_leverage_info(request)`
- `private_get_account_adjust_leverage_info(request)`
- `private_get_account_max_loan(request)`
- `private_get_account_trade_fee(request)`
- `private_get_account_interest_accrued(request)`
- `private_get_account_interest_rate(request)`
- `private_get_account_max_withdrawal(request)`
- `private_get_account_risk_state(request)`
- `private_get_account_interest_limits(request)`
- `private_get_account_spot_borrow_repay_history(request)`
- `private_get_account_greeks(request)`
- `private_get_account_position_tiers(request)`
- `private_get_account_set_account_switch_precheck(request)`
- `private_get_account_collateral_assets(request)`
- `private_get_account_mmp_config(request)`
- `private_get_account_move_positions_history(request)`
- `private_get_account_precheck_set_delta_neutral(request)`
- `private_get_account_quick_margin_borrow_repay_history(request)`
- `private_get_account_borrow_repay_history(request)`
- `private_get_account_vip_interest_accrued(request)`
- `private_get_account_vip_interest_deducted(request)`
- `private_get_account_vip_loan_order_list(request)`
- `private_get_account_vip_loan_order_detail(request)`
- `private_get_account_fixed_loan_borrowing_limit(request)`
- `private_get_account_fixed_loan_borrowing_quote(request)`
- `private_get_account_fixed_loan_borrowing_orders_list(request)`
- `private_get_account_spot_manual_borrow_repay(request)`
- `private_get_account_set_auto_repay(request)`
- `private_get_users_subaccount_list(request)`
- `private_get_account_subaccount_balances(request)`
- `private_get_asset_subaccount_balances(request)`
- `private_get_account_subaccount_max_withdrawal(request)`
- `private_get_asset_subaccount_bills(request)`
- `private_get_asset_subaccount_managed_subaccount_bills(request)`
- `private_get_users_entrust_subaccount_list(request)`
- `private_get_account_subaccount_interest_limits(request)`
- `private_get_users_subaccount_apikey(request)`
- `private_get_tradingbot_grid_orders_algo_pending(request)`
- `private_get_tradingbot_grid_orders_algo_history(request)`
- `private_get_tradingbot_grid_orders_algo_details(request)`
- `private_get_tradingbot_grid_sub_orders(request)`
- `private_get_tradingbot_grid_positions(request)`
- `private_get_tradingbot_grid_ai_param(request)`
- `private_get_tradingbot_signal_signals(request)`
- `private_get_tradingbot_signal_orders_algo_details(request)`
- `private_get_tradingbot_signal_orders_algo_pending(request)`
- `private_get_tradingbot_signal_orders_algo_history(request)`
- `private_get_tradingbot_signal_positions(request)`
- `private_get_tradingbot_signal_positions_history(request)`
- `private_get_tradingbot_signal_sub_orders(request)`
- `private_get_tradingbot_signal_event_history(request)`
- `private_get_tradingbot_recurring_orders_algo_pending(request)`
- `private_get_tradingbot_recurring_orders_algo_history(request)`
- `private_get_tradingbot_recurring_orders_algo_details(request)`
- `private_get_tradingbot_recurring_sub_orders(request)`
- `private_get_finance_savings_balance(request)`
- `private_get_finance_savings_lending_history(request)`
- `private_get_finance_staking_defi_offers(request)`
- `private_get_finance_staking_defi_orders_active(request)`
- `private_get_finance_staking_defi_orders_history(request)`
- `private_get_finance_staking_defi_eth_product_info(request)`
- `private_get_finance_staking_defi_eth_balance(request)`
- `private_get_finance_staking_defi_eth_purchase_redeem_history(request)`
- `private_get_finance_staking_defi_sol_product_info(request)`
- `private_get_finance_staking_defi_sol_balance(request)`
- `private_get_finance_staking_defi_sol_purchase_redeem_history(request)`
- `private_get_finance_flexible_loan_borrow_currencies(request)`
- `private_get_finance_flexible_loan_collateral_assets(request)`
- `private_get_finance_flexible_loan_max_collateral_redeem_amount(request)`
- `private_get_finance_flexible_loan_loan_info(request)`
- `private_get_finance_flexible_loan_loan_history(request)`
- `private_get_finance_flexible_loan_interest_accrued(request)`
- `private_get_copytrading_current_subpositions(request)`
- `private_get_copytrading_subpositions_history(request)`
- `private_get_copytrading_instruments(request)`
- `private_get_copytrading_profit_sharing_details(request)`
- `private_get_copytrading_total_profit_sharing(request)`
- `private_get_copytrading_unrealized_profit_sharing_details(request)`
- `private_get_copytrading_total_unrealized_profit_sharing(request)`
- `private_get_copytrading_config(request)`
- `private_get_copytrading_copy_settings(request)`
- `private_get_copytrading_current_lead_traders(request)`
- `private_get_copytrading_batch_leverage_info(request)`
- `private_get_copytrading_lead_traders_history(request)`
- `private_get_broker_dma_subaccount_info(request)`
- `private_get_broker_dma_subaccount_trade_fee(request)`
- `private_get_broker_dma_subaccount_apikey(request)`
- `private_get_broker_dma_rebate_per_orders(request)`
- `private_get_broker_fd_rebate_per_orders(request)`
- `private_get_broker_fd_if_rebate(request)`
- `private_get_broker_nd_info(request)`
- `private_get_broker_nd_subaccount_info(request)`
- `private_get_broker_nd_subaccount_apikey(request)`
- `private_get_asset_broker_nd_subaccount_deposit_address(request)`
- `private_get_asset_broker_nd_subaccount_deposit_history(request)`
- `private_get_asset_broker_nd_subaccount_withdrawal_history(request)`
- `private_get_broker_nd_rebate_daily(request)`
- `private_get_broker_nd_rebate_per_orders(request)`
- `private_get_finance_sfp_dcd_order(request)`
- `private_get_finance_sfp_dcd_orders(request)`
- `private_get_affiliate_invitee_detail(request)`
- `private_get_users_partner_if_rebate(request)`
- `private_get_support_announcements(request)`
- `private_post_rfq_create_rfq(request)`
- `private_post_rfq_cancel_rfq(request)`
- `private_post_rfq_cancel_batch_rfqs(request)`
- `private_post_rfq_cancel_all_rfqs(request)`
- `private_post_rfq_execute_quote(request)`
- `private_post_rfq_maker_instrument_settings(request)`
- `private_post_rfq_mmp_reset(request)`
- `private_post_rfq_mmp_config(request)`
- `private_post_rfq_create_quote(request)`
- `private_post_rfq_cancel_quote(request)`
- `private_post_rfq_cancel_batch_quotes(request)`
- `private_post_rfq_cancel_all_quotes(request)`
- `private_post_rfq_cancel_all_after(request)`
- `private_post_sprd_order(request)`
- `private_post_sprd_cancel_order(request)`
- `private_post_sprd_mass_cancel(request)`
- `private_post_sprd_amend_order(request)`
- `private_post_sprd_cancel_all_after(request)`
- `private_post_trade_order(request)`
- `private_post_trade_batch_orders(request)`
- `private_post_trade_cancel_order(request)`
- `private_post_trade_cancel_batch_orders(request)`
- `private_post_trade_amend_order(request)`
- `private_post_trade_amend_batch_orders(request)`
- `private_post_trade_close_position(request)`
- `private_post_trade_fills_archive(request)`
- `private_post_trade_cancel_advance_algos(request)`
- `private_post_trade_easy_convert(request)`
- `private_post_trade_one_click_repay(request)`
- `private_post_trade_one_click_repay_v2(request)`
- `private_post_trade_mass_cancel(request)`
- `private_post_trade_cancel_all_after(request)`
- `private_post_trade_order_precheck(request)`
- `private_post_trade_order_algo(request)`
- `private_post_trade_cancel_algos(request)`
- `private_post_trade_amend_algos(request)`
- `private_post_asset_transfer(request)`
- `private_post_asset_withdrawal(request)`
- `private_post_asset_withdrawal_lightning(request)`
- `private_post_asset_cancel_withdrawal(request)`
- `private_post_asset_convert_dust_assets(request)`
- `private_post_asset_monthly_statement(request)`
- `private_post_asset_convert_estimate_quote(request)`
- `private_post_asset_convert_trade(request)`
- `private_post_account_bills_history_archive(request)`
- `private_post_account_set_position_mode(request)`
- `private_post_account_set_leverage(request)`
- `private_post_account_position_margin_balance(request)`
- `private_post_account_set_fee_type(request)`
- `private_post_account_set_greeks(request)`
- `private_post_account_set_isolated_mode(request)`
- `private_post_account_spot_manual_borrow_repay(request)`
- `private_post_account_set_auto_repay(request)`
- `private_post_account_quick_margin_borrow_repay(request)`
- `private_post_account_borrow_repay(request)`
- `private_post_account_simulated_margin(request)`
- `private_post_account_position_builder(request)`
- `private_post_account_position_builder_graph(request)`
- `private_post_account_set_riskoffset_type(request)`
- `private_post_account_activate_option(request)`
- `private_post_account_set_auto_loan(request)`
- `private_post_account_account_level_switch_preset(request)`
- `private_post_account_set_account_level(request)`
- `private_post_account_set_collateral_assets(request)`
- `private_post_account_mmp_reset(request)`
- `private_post_account_mmp_config(request)`
- `private_post_account_fixed_loan_borrowing_order(request)`
- `private_post_account_fixed_loan_amend_borrowing_order(request)`
- `private_post_account_fixed_loan_manual_reborrow(request)`
- `private_post_account_fixed_loan_repay_borrowing_order(request)`
- `private_post_account_move_positions(request)`
- `private_post_account_set_auto_earn(request)`
- `private_post_account_set_settle_currency(request)`
- `private_post_account_set_trading_config(request)`
- `private_post_asset_subaccount_transfer(request)`
- `private_post_account_subaccount_set_loan_allocation(request)`
- `private_post_users_subaccount_create_subaccount(request)`
- `private_post_users_subaccount_apikey(request)`
- `private_post_users_subaccount_modify_apikey(request)`
- `private_post_users_subaccount_subaccount_apikey(request)`
- `private_post_users_subaccount_delete_apikey(request)`
- `private_post_users_subaccount_set_transfer_out(request)`
- `private_post_tradingbot_grid_order_algo(request)`
- `private_post_tradingbot_grid_amend_algo_basic_param(request)`
- `private_post_tradingbot_grid_amend_order_algo(request)`
- `private_post_tradingbot_grid_stop_order_algo(request)`
- `private_post_tradingbot_grid_close_position(request)`
- `private_post_tradingbot_grid_cancel_close_order(request)`
- `private_post_tradingbot_grid_order_instant_trigger(request)`
- `private_post_tradingbot_grid_withdraw_income(request)`
- `private_post_tradingbot_grid_compute_margin_balance(request)`
- `private_post_tradingbot_grid_margin_balance(request)`
- `private_post_tradingbot_grid_min_investment(request)`
- `private_post_tradingbot_grid_adjust_investment(request)`
- `private_post_tradingbot_signal_create_signal(request)`
- `private_post_tradingbot_signal_order_algo(request)`
- `private_post_tradingbot_signal_stop_order_algo(request)`
- `private_post_tradingbot_signal_margin_balance(request)`
- `private_post_tradingbot_signal_amendtpsl(request)`
- `private_post_tradingbot_signal_set_instruments(request)`
- `private_post_tradingbot_signal_close_position(request)`
- `private_post_tradingbot_signal_sub_order(request)`
- `private_post_tradingbot_signal_cancel_sub_order(request)`
- `private_post_tradingbot_recurring_order_algo(request)`
- `private_post_tradingbot_recurring_amend_order_algo(request)`
- `private_post_tradingbot_recurring_stop_order_algo(request)`
- `private_post_finance_savings_purchase_redempt(request)`
- `private_post_finance_savings_set_lending_rate(request)`
- `private_post_finance_staking_defi_purchase(request)`
- `private_post_finance_staking_defi_redeem(request)`
- `private_post_finance_staking_defi_cancel(request)`
- `private_post_finance_staking_defi_eth_purchase(request)`
- `private_post_finance_staking_defi_eth_redeem(request)`
- `private_post_finance_staking_defi_eth_cancel_redeem(request)`
- `private_post_finance_staking_defi_sol_purchase(request)`
- `private_post_finance_staking_defi_sol_redeem(request)`
- `private_post_finance_staking_defi_sol_cancel_redeem(request)`
- `private_post_finance_flexible_loan_max_loan(request)`
- `private_post_finance_flexible_loan_adjust_collateral(request)`
- `private_post_copytrading_algo_order(request)`
- `private_post_copytrading_close_subposition(request)`
- `private_post_copytrading_set_instruments(request)`
- `private_post_copytrading_amend_profit_sharing_ratio(request)`
- `private_post_copytrading_first_copy_settings(request)`
- `private_post_copytrading_amend_copy_settings(request)`
- `private_post_copytrading_stop_copy_trading(request)`
- `private_post_copytrading_batch_set_leverage(request)`
- `private_post_broker_nd_create_subaccount(request)`
- `private_post_broker_nd_delete_subaccount(request)`
- `private_post_broker_nd_subaccount_apikey(request)`
- `private_post_broker_nd_subaccount_modify_apikey(request)`
- `private_post_broker_nd_subaccount_delete_apikey(request)`
- `private_post_broker_nd_set_subaccount_level(request)`
- `private_post_broker_nd_set_subaccount_fee_rate(request)`
- `private_post_broker_nd_set_subaccount_assets(request)`
- `private_post_asset_broker_nd_subaccount_deposit_address(request)`
- `private_post_asset_broker_nd_modify_subaccount_deposit_address(request)`
- `private_post_broker_nd_rebate_per_orders(request)`
- `private_post_finance_sfp_dcd_quote(request)`
- `private_post_finance_sfp_dcd_order(request)`
- `private_post_broker_nd_report_subaccount_ip(request)`
- `private_post_broker_dma_subaccount_apikey(request)`
- `private_post_broker_dma_trades(request)`
- `private_post_broker_fd_rebate_per_orders(request)`

### WS Unified

- `describe(self)`
- `get_url(self, channel: str, access='public')`
- `subscribe_multiple(self, access, channel, symbols: Strings = None, params={})`
- `subscribe(self, access, messageHash, channel, symbol, params={})`
- `watch_trades(self, symbol: str, since: Int = None, limit: Int = None, params={})`
- `watch_trades_for_symbols(self, symbols: List[str], since: Int = None, limit: Int = None, params={})`
- `un_watch_trades_for_symbols(self, symbols: List[str], params={})`
- `un_watch_trades(self, symbol: str, params={})`
- `watch_funding_rate(self, symbol: str, params={})`
- `watch_funding_rates(self, symbols: List[str], params={})`
- `watch_ticker(self, symbol: str, params={})`
- `un_watch_ticker(self, symbol: str, params={})`
- `watch_tickers(self, symbols: Strings = None, params={})`
- `watch_mark_price(self, symbol: str, params={})`
- `watch_mark_prices(self, symbols: Strings = None, params={})`
- `un_watch_tickers(self, symbols: Strings = None, params={})`
- `watch_bids_asks(self, symbols: Strings = None, params={})`
- `watch_liquidations_for_symbols(self, symbols: List[str], since: Int = None, limit: Int = None, params={})`
- `watch_my_liquidations_for_symbols(self, symbols: List[str], since: Int = None, limit: Int = None, params={})`
- `watch_ohlcv(self, symbol: str, timeframe: str = '1m', since: Int = None, limit: Int = None, params={})`
- `un_watch_ohlcv(self, symbol: str, timeframe: str = '1m', params={})`
- `watch_ohlcv_for_symbols(self, symbolsAndTimeframes: List[List[str]], since: Int = None, limit: Int = None, params={})`
- `un_watch_ohlcv_for_symbols(self, symbolsAndTimeframes: List[List[str]], params={})`
- `watch_order_book(self, symbol: str, limit: Int = None, params={})`
- `watch_order_book_for_symbols(self, symbols: List[str], limit: Int = None, params={})`
- `un_watch_order_book_for_symbols(self, symbols: List[str], params={})`
- `un_watch_order_book(self, symbol: str, params={})`
- `authenticate(self, params={})`
- `watch_balance(self, params={})`
- `order_to_trade(self, order, market=None)`
- `watch_my_trades(self, symbol: Str = None, since: Int = None, limit: Int = None, params={})`
- `watch_positions(self, symbols: Strings = None, since: Int = None, limit: Int = None, params={})`
- `watch_orders(self, symbol: Str = None, since: Int = None, limit: Int = None, params={})`
- `create_order_ws(self, symbol: str, type: OrderType, side: OrderSide, amount: float, price: Num = None, params={})`
- `edit_order_ws(self, id: str, symbol: str, type: OrderType, side: OrderSide, amount: Num = None, price: Num = None, params={})`
- `cancel_order_ws(self, id: str, symbol: Str = None, params={})`
- `cancel_orders_ws(self, ids: List[str], symbol: Str = None, params={})`
- `cancel_all_orders_ws(self, symbol: Str = None, params={})`

## Contribution
- Give us a star :star:
- Fork and Clone! Awesome
- Select existing issues or create a new issue.