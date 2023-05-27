SELECT customer_id, AVG(amount) AS average_amount, MAX(amount) AS max_amount, MIN(amount) AS min_amount
FROM payment
WHERE customer_id BETWEEN 350 AND 400 AND payment_date BETWEEN '2007-02-16' AND '2007-02-20'
GROUP BY customer_id
ORDER BY customer_id DESC;
