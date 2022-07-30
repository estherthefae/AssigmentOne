import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

CHROME_DRIVER_PATH = "C:\\Development\\chromedriver.exe"
service = Service(CHROME_DRIVER_PATH)
driver = webdriver.Chrome(service=service)


# BINCOM INTERMEDIATE ASSIGNMENT WEEK ONE

# ASSIGNMENT 1
# Scrape books from http://books.toscrape.com
# (Book name, price, stock status (in stock or out of stock), rating, description, product information,
# category (poetry, fiction, historical fiction, etc)
# Scrape the first 5 pages (20 books per page)

# SOLUTION
def question_one():
    driver.get(url="http://books.toscrape.com")

    def convert(string):
        if string == "One":
            return 1
        elif string == "Two":
            return 2
        elif string == 3:
            return 3
        elif string == 4:
            return 4
        elif string == 5:
            return 5

    book_names = []
    book_prices = []
    stock_status = []
    book_rating = []
    book_description = []
    book_category = []

    book_links = []
    for i in range(2):
        books = driver.find_elements(By.CSS_SELECTOR, ".product_pod h3 a")
        for book in books:
            book_links.append(book.text)
        driver.find_element(By.LINK_TEXT, 'next').click()
        time.sleep(3)

    driver.get(url="http://books.toscrape.com")
    count = 0
    heads = []
    data = []

    for link in book_links:
        info = driver.find_element(By.LINK_TEXT, link)
        info.click()
        book_names.append(driver.find_element(By.CSS_SELECTOR, ".product_main h1").text)
        book_prices.append(driver.find_element(By.CSS_SELECTOR, ".product_main .price_color").text)
        stock_status.append(driver.find_element(By.CSS_SELECTOR, ".product_main .instock").text)
        book_rating.append(convert(
            driver.find_element(By.XPATH, '//*[@id="content_inner"]/article/div[1]/div[2]/p[3]').get_attribute(
                'class').split(" ")[1]))
        book_description.append(driver.find_element(By.CSS_SELECTOR, "#content_inner p").text)
        if count < 1:
            product_info_head = (driver.find_elements(By.CSS_SELECTOR, "#content_inner th"))
            heads = [head.text for head in product_info_head]
        product_info_data = (driver.find_elements(By.CSS_SELECTOR, "#content_inner td"))
        data.append([body.text for body in product_info_data])
        book_category.append(driver.find_element(By.XPATH, '//*[@id="default"]/div/div/ul/li[3]/a').text)
        driver.get(url="http://books.toscrape.com")
        if count < 20:
            no_of_next = count // 19
        else:
            no_of_next = count // 20
        if no_of_next > 0:
            for _ in range(no_of_next):
                driver.find_element(By.LINK_TEXT, 'next').click()
                time.sleep(2)
        count += 1

    book_info = []
    info = []
    for body in data:
        for i in range(len(body)):
            info.append(f"{heads[i]}: {body[i]}")
        book_info.append(info)
        info = []

    book_information = []
    for info in book_info:
        combined = '\n\t'.join(info)
        book_information.append(combined)

    book_details = []
    for count in range(len(book_links)):
        book_details.append(f"Book Name: {book_names[count]}\n"
                            f"Book Price: {book_prices[count]}\n"
                            f"Book Stock Status: {stock_status[count]}\n"
                            f"Book Rating: {book_rating[count]} stars out of 5\n"
                            f"Book Description: {book_description[count]}\n"
                            f"Book Information:\n\t {book_information[count]}\n"
                            f"Book Category: {book_category[count]}")

    with open(file="question_one.txt", mode='w') as file:
        for detail in book_details:
            print(detail)
            file.write(detail)
            print('\n')
            file.write('\n')
            print('\n')
            file.write('\n')


# ASSIGNMENT 2
# Scrape 10-20 distinct quote authors from http://quotes.toscrape.com
# (Name, nationality, description, date of birth)

# SOLUTION
def question_two():
    driver.get(url="http://quotes.toscrape.com/")
    author_names = []
    unique_names = []
    while len(unique_names) < 20:
        names = driver.find_elements(By.CLASS_NAME, "author")
        author_names += [name.text for name in names]
        unique_names = set(author_names)
        time.sleep(2)
        next_page = driver.find_element(By.CSS_SELECTOR, '.pager .next a')
        next_page.click()
    author_names = list(unique_names)[:21]
    name_of_author = []
    date_of_birth = []
    nationality = []
    description = []
    for name in author_names:
        driver.get(url=f"http://quotes.toscrape.com/author/{name.replace(' ', '-')}")
        name_of_author.append(driver.find_element(By.CLASS_NAME, 'author-title').text)
        date_of_birth.append(driver.find_element(By.CLASS_NAME, 'author-born-date').text)
        nationality.append(driver.find_element(By.CLASS_NAME, 'author-born-location').text[2:])
        description.append(driver.find_element(By.CLASS_NAME, 'author-description').text)
    print("Here are the lists of the authors")
    for num in range(len(author_names)):
        print(name_of_author[num])
        print(date_of_birth[num])
        print(nationality[num])
        print(description[num])
        print('\n')
    author_details = []
    for count in range(len(author_names)):
        author_details.append(f"Author Name: {name_of_author[count]}\n"
                              f"Date of Birth: {date_of_birth[count]}\n"
                              f"Nationality: {nationality[count]}\n"
                              f"Description: {description[count]}\n\n")
    # Writing information to a file
    with open(file="question_two.txt", mode='w') as file:
        for detail in author_details:
            file.write(detail)


question_two()


# ASSIGNMENT 3
# Build a scraper that will scrape a random page from Wikipedia

# SOLUTION
def question_three():
    driver.get(url="https://www.wikipedia.org/")
    search = driver.find_element(By.ID, 'searchInput')
    search.send_keys("Love")
    search.send_keys(Keys.ENTER)
    # EXTRACTING FROM THE SITE ON LOVE
    title = driver.find_element(By.ID, "firstHeading").text.upper()
    reference = driver.find_element(By.ID, "siteSub").text
    content = driver.find_element(By.CSS_SELECTOR, ".mw-parser-output p")
    print(title)
    print(reference)
    print(content)


question_two()
