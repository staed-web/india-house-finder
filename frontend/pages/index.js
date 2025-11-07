import { useState, useEffect } from 'react';
import Head from 'next/head';

export default function Home() {
  const [listings, setListings] = useState([]);
  const [filters, setFilters] = useState({
    city: 'bangalore',
    min_price: 5000,
    max_price: 50000,
    bedrooms: '',
    property_type: 'all'
  });

  useEffect(() => {
    fetchListings();
  }, []);

  const fetchListings = async () => {
    const qs = new URLSearchParams(filters).toString();
    const res = await fetch(`https://your-render-url.onrender.com/listings?${qs}`);
    const data = await res.json();
    setListings(data.listings);
  };

  return (
    <div className="container">
      <Head>
        <title>India House Finder - Rent & Buy Flats</title>
        <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=YOUR_ADSENSE_ID" crossOrigin="anonymous"></script>
      </Head>

      <header>
        <h1>🏠 Find Your Home in India</h1>
        <p>Aggregated listings from MagicBricks, NoBroker & more</p>
      </header>

      {/* AdSense Banner */}
      <ins className="adsbygoogle"
           style={{ display: 'block' }}
           data-ad-client="ca-pub-YOUR_ADSENSE_ID"
           data-ad-slot="1234567890"
           data-ad-format="auto"></ins>

      <div className="filters">
        <input value={filters.city} onChange={e => setFilters({...filters, city: e.target.value})} placeholder="City" />
        <input type="number" value={filters.min_price} onChange={e => setFilters({...filters, min_price: e.target.value})} placeholder="Min Rent (₹)" />
        <input type="number" value={filters.max_price} onChange={e => setFilters({...filters, max_price: e.target.value})} placeholder="Max Rent (₹)" />
        <select value={filters.bedrooms} onChange={e => setFilters({...filters, bedrooms: e.target.value})}>
          <option value="">Any BHK</option>
          <option value="1">1 BHK</option>
          <option value="2">2 BHK</option>
          <option value="3">3 BHK</option>
        </select>
        <button onClick={fetchListings}>Search</button>
      </div>

      <div className="listings">
        {listings.map(listing => (
          <div key={listing.id} className="listing-card">
            <h3>{listing.title || `${listing.bedrooms} BHK in ${listing.location}`}</h3>
            <p>₹{listing.price.toLocaleString('en-IN')} • {listing.platform}</p>
            <a href={listing.url} target="_blank" rel="nofollow">View on {listing.platform}</a>
          </div>
        ))}
      </div>

      {/* AdSense In-Content */}
      <ins className="adsbygoogle"
           style={{ display: 'block', marginTop: '20px' }}
           data-ad-client="ca-pub-YOUR_ADSENSE_ID"
           data-ad-slot="0987654321"
           data-ad-format="fluid"></ins>
    </div>
  );
}
