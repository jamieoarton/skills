# Edit Space Tag

Update a task Tag.

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
    "/v2/space/{space_id}/tag/{tag_name}": {
      "put": {
        "summary": "Edit Space Tag",
        "tags": [
          "Tags"
        ],
        "description": "Update a task Tag.",
        "operationId": "EditSpaceTag",
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
                512
              ]
            }
          },
          {
            "name": "tag_name",
            "in": "path",
            "description": "",
            "required": true,
            "style": "simple",
            "schema": {
              "type": "string",
              "examples": [
                "name"
              ]
            }
          }
        ],
        "requestBody": {
          "description": "",
          "content": {
            "application/json": {
              "schema": {
                "title": "EditSpaceTagrequest",
                "required": [
                  "tag"
                ],
                "type": "object",
                "properties": {
                  "tag": {
                    "title": "Tag1",
                    "required": [
                      "name",
                      "fg_color",
                      "bg_color"
                    ],
                    "type": "object",
                    "properties": {
                      "name": {
                        "type": "string"
                      },
                      "fg_color": {
                        "type": "string"
                      },
                      "bg_color": {
                        "type": "string"
                      }
                    },
                    "examples": [
                      {
                        "name": "Updated Tag",
                        "fg_color": "#ffffff",
                        "bg_color": "#ffffff"
                      }
                    ]
                  }
                },
                "examples": [
                  {
                    "tag": {
                      "name": "Updated Tag",
                      "fg_color": "#ffffff",
                      "bg_color": "#ffffff"
                    }
                  }
                ]
              },
              "example": {
                "tag": {
                  "name": "Tag name",
                  "tag_fg": "#000000",
                  "tag_bg": "#000000"
                }
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
                  "title": "EditSpaceTagresponse",
                  "required": [
                    "tag"
                  ],
                  "type": "object",
                  "properties": {
                    "tag": {
                      "$ref": "#/paths/~1v2~1space~1%7Bspace_id%7D~1tag~1%7Btag_name%7D/put/requestBody/content/application~1json/schema/properties/tag"
                    }
                  },
                  "examples": [
                    {
                      "tag": {
                        "name": "Updated Tag",
                        "fg_color": "#ffffff",
                        "bg_color": "#ffffff"
                      }
                    }
                  ]
                },
                "example": {
                  "tag": {
                    "name": "Updated Tag",
                    "fg_color": "#ffffff",
                    "bg_color": "#ffffff"
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
      "name": "Tags"
    }
  ]
}
```