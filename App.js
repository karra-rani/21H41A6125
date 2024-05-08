import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
function App() {
  return (
    <Router>
      {/* Your app content */}
    </Router>
  );
}

javascript
function App() {
  return (
    <Router>
      <Switch>
        {/* Routes */}
      </Switch>
    </Router>
  );
}

function App() {
  return (
    <Router>
      <Switch>
        <Route exact path="/" component={AllProductsPage} />
        <Route path="/product/:id" component={SpecificProductPage} />
      </Switch>
    </Router>
  );
}




