CREATE TABLE entertainment_exchange1(
    id int primary key,
    Type text, 
    name text,
    price text,
    country text
);

INSERT INTO entertainment_exchange1(id,Type,name,price,country) VALUES
(187760,"News","Hackers in Dubai","$8.49","Dubai"),
(187761,"Book","Jamie Oliver","$9.99","England"),
(187762,"Movie","Star Wars","$8.49","USA"),
(187763,"Movie","Two and a half men","$8.49","USA"),
(187764,"News","Hackers monthly","FREE","Aus"),
(187765,"News","Rolex releases new watch","$5.50","Switzerland"),
(187766,"Book","Guide to the galaxy","$11.59","England"),
(187767,"News","Hackers alert","FREE","WORLD"),
(187768,"Game","Fortnite","FREE","Aus"),
(187769,"News","Unrest in Minniapolis","$2.99","USA"),
(187770,"Unknown","Unknown","Unknown","Unknown"),
(187771,"Book","UFC","$1.99","Aus");


SELECT Type, COUNT(*) FROM entertainment_exchange1 GROUP BY Type;


SELECT Type, COUNT(*) AS total_items FROM entertainment_exchange1 WHERE name LIKE "Hackers%" GROUP BY Type;

SELECT *
FROM entertainment_exchange1
ORDER BY 
    CASE 
        WHEN price = "FREE" THEN 0
        WHEN price = "Unknown" THEN NULL
        ELSE CAST(REPLACE(price, "$", "") AS DECIMAL(10,2))
    END DESC;
