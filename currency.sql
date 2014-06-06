SELECT DISTINCT ON (currency.id) 
    currency.currency_code,
    currency_value.exchange_rate,
    currency_value.date
FROM 
currency_value INNER JOIN currency
ON currency_value.currency_id = currency.id

ORDER BY currency.id, currency_value.date DESC

