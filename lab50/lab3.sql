-- Names starting with 'M'
SELECT * FROM staff
WHERE full_name LIKE 'M%';

-- Names containing 'son'
SELECT * FROM staff
WHERE full_name LIKE '%son%';

-- Names ending with 'r'
SELECT * FROM staff
WHERE full_name LIKE '%r';
