```JavaScript
// Node
require "http"
let request = http.get("https://jake.dev/a.csv", function(response) {
  // csv parser
}
```

```Java
// Java
import java.io.BufferedInput;
import java.net.URL;
var csv = new BufferedInput(new URL("https://jake.dev/a.csv"));
```

```C#
// C#
using System.Net;
var csv = new WebClient("https://jake.dev/a.csv", "my.csv");
```

```Rust
// Rust
let mut csv = request::get("https://jake.dev/a.csv");
```

```Ruby
# Ruby
require "open-uri"

open("https://jake.dev/a.csv") do |file|
  # whatever you want to do
end
```