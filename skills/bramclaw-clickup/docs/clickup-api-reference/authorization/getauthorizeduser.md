# Get Authorized User

View the details of the authenticated user's ClickUp account.

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
    "/v2/user": {
      "get": {
        "summary": "Get Authorized User",
        "tags": [
          "Authorization"
        ],
        "description": "View the details of the authenticated user's ClickUp account.",
        "operationId": "GetAuthorizedUser",
        "parameters": [],
        "responses": {
          "200": {
            "description": "",
            "headers": {},
            "content": {
              "application/json": {
                "schema": {
                  "title": "GetAuthorizedUserresponse",
                  "type": "object",
                  "properties": {
                    "user": {
                      "title": "User",
                      "type": "object",
                      "properties": {
                        "id": {
                          "type": "integer",
                          "contentEncoding": "int32"
                        },
                        "username": {
                          "type": "string"
                        },
                        "email": {
                          "type": "string"
                        },
                        "color": {
                          "type": "string"
                        },
                        "profilePicture": {
                          "type": "string"
                        },
                        "initials": {
                          "type": "string"
                        },
                        "week_start_day": {
                          "type": "integer",
                          "contentEncoding": "int32",
                          "description": "The user's preferred start of the calendar week setting. \\ `0` is Sunday. \\ `1` is Monday."
                        },
                        "global_font_support": {
                          "type": "boolean"
                        },
                        "timezeone": {
                          "type": "string"
                        }
                      },
                      "examples": [
                        {
                          "id": 123,
                          "username": "John Doe",
                          "email": "user@company.com",
                          "color": "#000000",
                          "profilePicture": "https://clickup.com/avatar.jpg",
                          "initials": "JD",
                          "week_start_day": 0,
                          "global_font_support": false,
                          "timezone": "America/Los_Angeles"
                        }
                      ]
                    }
                  },
                  "examples": [
                    {
                      "user": {
                        "id": 123,
                        "username": "John Doe",
                        "email": "user@company.com",
                        "color": "#000000",
                        "profilePicture": "https://clickup.com/avatar.jpg",
                        "initials": "JD",
                        "week_start_day": 0,
                        "global_font_support": false,
                        "timezone": "America/Los_Angeles"
                      }
                    }
                  ]
                },
                "example": {
                  "user": {
                    "id": 123,
                    "username": "John Doe",
                    "email": "user@company.com",
                    "color": "#000000",
                    "profilePicture": "https://clickup.com/avatar.jpg",
                    "initials": "JD",
                    "week_start_day": 0,
                    "global_font_support": false,
                    "timezone": "America/Los_Angeles"
                  }
                }
              }
            }
          }
        },
        "deprecated": false
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