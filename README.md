# custom-webhook-splunk
custom webhook for splunk with custom payload and headers support for alerts.

Splunk is wonderful with loads of features, yet a few of the features are not available out-of-the-box, one of those missing features is the customizable webhook alert action.

While working on a project I needed to send some custom metrics along with some headers from Splunk alerts and ended up exploring the default available webhook alert action.

This is what’s already available:
Splunk by default provides webhook alert action for an alert however, it is lacking some of the required features like:

-	Authentication mechanism
-	Custom header support
-	Custom payload support

Above features being missing from the default webhook alert action on Splunk makes it very less useful because mostly the webhooks require some kind of authentication to receive the data and similarly customized payload might be a requirement for some webhook APIs.

Splunk has done a great job with their pluggable platform that you can write your own apps and deploy them to serve your custom requirements however, building a custom app can be tricky and time consuming.

After reviewing the webhook alert action I decided to develop my own custom webhook alert action with all the required missing features.

This customWebhhok alert action application works with the following configurable options:

url: Target webhook url
  `e.g. https://server.com/api/v2/webhook`

Headers (dict): Include any number of headers
  `e.g. {‘Authorization’: ‘Bearer <token>’, ‘Content-Type’: ‘application/json’…}`

Payload (dict): Payload data with key-value pairs of your choice
  `e.g. {‘service_name’: ‘MyService’, ‘key1’: ‘value1’, ‘key2’: ‘value2’…}`

**Contributing**
Contributions are welcomed! Read the [Contributing Guide](../CONTRIBUTING.md) for more information.

**Licensing**
This project is licensed under the MIT License. See [License](../LICENSE.md) for more information.
