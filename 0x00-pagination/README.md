# 0x00. Pagination

## Advanced RESTUL API Concepts
    - REST API Design: Pagination
    - HATEOAS
## Tasks
### 0. Simple helper function

Function named index_range that takes two integer arguments page and page_size.

It returns a tuple of size two containing a start index and an end index corresponding to the range of indexes to return in a list for those particular pagination parameters.

Page numbers are 1-indexed, i.e. the first page is page 1.


### 1. Simple pagination

Continuing from previous code:
Method named get_page that takes two integer arguments page with default value 1 and page_size with default value 10.

    - Uses assert to verify that both arguments are integers greater than 0.
    - Uses index_range to find the correct indexes to paginate the dataset correctly and return the appropriate page of the dataset (i.e. the correct list of rows).
    - If the input arguments are out of range for the dataset, an empty list is returned


### 2. Hypermedia pagination 

Implements a get_hyper method that takes the same arguments (and defaults) as get_page and returns a dictionary containing the following key-value pairs:

    - page_size: the length of the returned dataset page
    - page: the current page number
    - data: the dataset page (equivalent to return from previous task)
    - next_page: number of the next page, None if no next page
    - prev_page: number of the previous page, None if no previous page
    - total_pages: the total number of pages in the dataset as an integer

