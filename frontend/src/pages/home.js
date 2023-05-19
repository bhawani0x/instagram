import React, { useEffect, useState } from 'react';
import './home.css';

const HomePage = () => {
  const [data, setData] = useState(null);
  const [filterCategory, setFilterCategory] = useState('');
  const [filterCategories, setFilterCategories] = useState([]);
  const [filterTag, setFilterTag] = useState('');
  const [filterTags, setFilterTags] = useState([]);
  let serialNumber = 1;

  useEffect(() => {
    fetch('http://localhost:8000/api/data/photo/') // Replace with your actual endpoint URL
      .then(response => response.json())
      .then(data => {
        const categories = new Set(data.flatMap(item => item.category_name));
        setData(data);
        setFilterCategories(Array.from(categories));
      })
      .catch(error => console.log(error));
  }, []);

  useEffect(() => {
    if (data) {
      const filteredCategories = data.filter(item => item.category_name.includes(filterCategory));
      const tags = new Set(filteredCategories.flatMap(item => item.tag_name));
      setFilterTags(Array.from(tags));
    }
  }, [filterCategory, data]);

  const handleDownload = (url, filename) => {
    fetch(url)
      .then(response => response.blob())
      .then(blob => {
        const blobURL = URL.createObjectURL(blob);
        const link = document.createElement('a');
        link.href = blobURL;
        link.download = filename;
        link.click();
      })
      .catch(error => console.log(error));
  };

  const handleCategoryChange = event => {
    setFilterCategory(event.target.value);
  };

  const handleTagChange = event => {
    setFilterTag(event.target.value);
  };

  if (!data) {
    return <p>Loading...</p>;
  }

  const filteredData = filterCategory
    ? data.filter(item => item.category_name.includes(filterCategory))
        .filter(item => filterTag ? item.tag_name.includes(filterTag) : true)
    : data.filter(item => filterTag ? item.tag_name.includes(filterTag) : true);

  return (
    <div>
      <h1>Post Details</h1>
      <div className="filter-container">
        <label htmlFor="category">Filter by Category:</label>
        <select id="category" value={filterCategory} onChange={handleCategoryChange}>
          <option value="">All</option>
          {filterCategories.map(category => (
            <option key={category} value={category}>
              {category}
            </option>
          ))}
        </select>
        <label htmlFor="tag">Filter by Tag:</label>
        <select id="tag" value={filterTag} onChange={handleTagChange}>
          <option value="">All</option>
          {filterTags.map(tag => (
            <option key={tag} value={tag}>
              {tag}
            </option>
          ))}
        </select>
      </div>
      <div className="table-container">
        <table>
          <thead>
            <tr>
              <th>Serial Number</th>
              <th>Category Name</th>
              <th>Insta Name</th>
              <th>Post</th>
              <th>Tags</th>
              <th>Likes</th>
              <th>Action</th>
            </tr>
          </thead>
          <tbody>
            {filteredData.map(item => (
              <tr key={item.id}>
                <td>{serialNumber++}</td>
                <td>{item.category_name.join(', ')}</td>
                <td>{item.photo_name}</td>
                <td>
                  <a href={item.insta_post} target="_blank" rel="noopener noreferrer">
                    <img src={item.insta_post} alt="Post" />
                  </a>
                </td>
                <td>{item.tag_name.join(', ')}</td>
                <td>{item.post_like}</td>
                <td>
                  <button onClick={() => handleDownload(item.insta_post, item.photo_name)}>
                    Download
                  </button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default HomePage;
