# Get Access Token

These are the routes for authing the API and going through the [OAuth flow](doc:authentication).\
 \
Applications utilizing a personal API token don't use this endpoint.\
 \
***Note:** OAuth tokens are not supported when using the [**Try It** feature](doc:trytheapi) of our Reference docs. You can't try this endpoint from your web browser.*


# OpenAPI definition

```json
{
  "openapi": "3.1.0",
  "info": {
    "title": "ClickUp API v2 Reference",
    "description": "The ClickUp API enables you to programmatically access and manage your ClickUp resources.\n\n## Authentication\nThe API supports two authentication methods:\n- **Personal API Token**: Use for testing and personal integrations. Add token to requests with header: `Authorization: pk_...`\n- **OAuth 2.0**: Required for building apps for other users. Uses authorization code flow.\n\n## Getting Started\nOur [Getting Started Guide](https://developer.clickup.com/docs/index) provides a comprehensive overview of how to use the ClickUp API.\n",
    "contact": {},
    "version": "2.0"
  },
  "jsonSchemaDialect": "https://json-schema.org/draft/2020-12/schema",
  "servers": [
    {
      "url": "https://api.clickup.com/api",
      "description": "ClickUp",
      "variables": {}
    }
  ],
  "paths": {
    "/v2/oauth/token": {
      "post": {
        "summary": "Get Access Token",
        "tags": [
          "Authorization"
        ],
        "description": "These are the routes for authing the API and going through the [OAuth flow](https://developer.clickup.com/docs/authentication).\\\n \\\nApplications utilizing a personal API token don't use this endpoint.\\\n \\\n***Note:** OAuth tokens are not supported when using the [**Try It** feature](https://developer.clickup.com/docs/trytheapi) of our Reference docs. You can't try this endpoint from your web browser.*\n",
        "operationId": "GetAccessToken",
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "title": "GetAccessTokenrequest",
                "required": [
                  "client_id",
                  "client_secret",
                  "code"
                ],
                "type": "object",
                "properties": {
                  "client_id": {
                    "type": "string",
                    "description": "OAuth app client id"
                  },
                  "client_secret": {
                    "type": "string",
                    "description": "OAuth app client secret"
                  },
                  "code": {
                    "type": "string",
                    "description": "Code given in redirect url"
                  }
                },
                "examples": [
                  {
                    "client_id": "your_client_id",
                    "client_secret": "your_client_secret",
                    "code": "authorization_code"
                  }
                ]
              },
              "example": {
                "client_id": "your_client_id",
                "client_secret": "your_client_secret",
                "code": "authorization_code"
              }
            },
            "application/x-www-form-urlencoded": {
              "schema": {
                "$ref": "#/paths/~1v2~1oauth~1token/post/requestBody/content/application~1json/schema"
              },
              "example": {
                "client_id": "your_client_id",
                "client_secret": "your_client_secret",
                "code": "authorization_code"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "",
            "headers": {},
            "content": {
              "application/json": {
                "schema": {
                  "title": "GetAccessTokenresponse",
                  "required": [
                    "access_token"
                  ],
                  "type": "object",
                  "properties": {
                    "access_token": {
                      "type": "string"
                    }
                  },
                  "examples": [
                    {
                      "access_token": "access token"
                    }
                  ]
                },
                "example": {
                  "access_token": "access token"
                }
              }
            }
          }
        },
        "deprecated": false,
        "security": [],
        "x-hideTryItPanel": true
      },
      "parameters": []
    }
  },
  "components": {
    "securitySchemes": {
      "Authorization_Token": {
        "name": "Authorization",
        "type": "apiKey",
        "in": "header",
        "description": "API token required for authentication. Two types of tokens are supported:\n**Personal API Key** Obtain from ClickUp's settings page under 'Apps' and add it to the header as `Authorization: pk_...`\n**OAuth2 Access Token** Generated through the OAuth2 flow and add it to the header as `Authorization: Bearer {access_token}`"
      }
    }
  },
  "security": [
    {
      "Authorization_Token": []
    }
  ],
  "tags": [
    {
      "name": "Authorization"
    }
  ]
}
```