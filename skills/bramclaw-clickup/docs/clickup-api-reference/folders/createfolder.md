# Create Folder

Add a new Folder to a Space.

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
    "/v2/space/{space_id}/folder": {
      "post": {
        "summary": "Create Folder",
        "tags": [
          "Folders"
        ],
        "description": "Add a new Folder to a Space.",
        "operationId": "CreateFolder",
        "parameters": [
          {
            "name": "space_id",
            "in": "path",
            "description": "",
            "required": true,
            "style": "simple",
            "schema": {
              "type": "number",
              "contentEncoding": "double",
              "examples": [
                789
              ]
            }
          }
        ],
        "requestBody": {
          "description": "",
          "content": {
            "application/json": {
              "schema": {
                "title": "CreateFolderrequest",
                "required": [
                  "name"
                ],
                "type": "object",
                "properties": {
                  "name": {
                    "type": "string"
                  }
                },
                "examples": [
                  {
                    "name": "New Folder Name"
                  }
                ]
              },
              "example": {
                "name": "New Folder Name"
              }
            }
          },
          "required": true
        },
        "responses": {
          "200": {
            "description": "",
            "headers": {},
            "content": {
              "application/json": {
                "schema": {
                  "title": "CreateFolderresponse",
                  "required": [
                    "id",
                    "name",
                    "orderindex",
                    "override_statuses",
                    "hidden",
                    "space",
                    "task_count"
                  ],
                  "type": "object",
                  "properties": {
                    "id": {
                      "type": "string"
                    },
                    "name": {
                      "type": "string"
                    },
                    "orderindex": {
                      "type": "integer",
                      "contentEncoding": "int32"
                    },
                    "override_statuses": {
                      "type": "boolean"
                    },
                    "hidden": {
                      "type": "boolean"
                    },
                    "space": {
                      "$ref": "#/paths/~1v2~1list~1%7Blist_id%7D/get/responses/200/content/application~1json/schema/properties/space"
                    },
                    "task_count": {
                      "type": "string"
                    }
                  },
                  "examples": [
                    {
                      "id": "457",
                      "name": "New Folder Name",
                      "orderindex": 0,
                      "override_statuses": false,
                      "hidden": false,
                      "space": {
                        "id": "789",
                        "name": "Space Name",
                        "access": true
                      },
                      "task_count": "0"
                    }
                  ]
                },
                "example": {
                  "id": "457",
                  "name": "New Folder Name",
                  "orderindex": 0,
                  "override_statuses": false,
                  "hidden": false,
                  "space": {
                    "id": "789",
                    "name": "Space Name",
                    "access": true
                  },
                  "task_count": "0"
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
      "name": "Folders"
    }
  ]
}
```