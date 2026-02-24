# Get Space

View the Spaces available in a Workspace.

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
    "/v2/space/{space_id}": {
      "get": {
        "summary": "Get Space",
        "tags": [
          "Spaces"
        ],
        "description": "View the Spaces available in a Workspace.",
        "operationId": "GetSpace",
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
                790
              ]
            }
          }
        ],
        "responses": {
          "200": {
            "description": "",
            "headers": {},
            "content": {
              "application/json": {
                "schema": {
                  "title": "GetSpaceresponse",
                  "required": [
                    "id",
                    "name",
                    "private",
                    "statuses",
                    "multiple_assignees",
                    "features"
                  ],
                  "type": "object",
                  "properties": {
                    "id": {
                      "type": "string"
                    },
                    "name": {
                      "type": "string"
                    },
                    "private": {
                      "type": "boolean"
                    },
                    "statuses": {
                      "type": "array",
                      "items": {
                        "$ref": "#/paths/~1v2~1task~1%7Btask_id%7D/get/responses/200/content/application~1json/schema/properties/status"
                      },
                      "description": ""
                    },
                    "multiple_assignees": {
                      "type": "boolean"
                    },
                    "features": {
                      "$ref": "#/paths/~1v2~1space~1%7Bspace_id%7D/put/requestBody/content/application~1json/schema/properties/features"
                    }
                  },
                  "examples": [
                    {
                      "id": "790",
                      "name": "Updated Space Name",
                      "private": false,
                      "statuses": [
                        {
                          "status": "to do",
                          "type": "open",
                          "orderindex": 0,
                          "color": "#d3d3d3"
                        },
                        {
                          "status": "complete",
                          "type": "closed",
                          "orderindex": 1,
                          "color": "#6bc950"
                        }
                      ],
                      "multiple_assignees": false,
                      "features": {
                        "due_dates": {
                          "enabled": false,
                          "start_date": false,
                          "remap_due_dates": false,
                          "remap_closed_due_date": false
                        },
                        "time_tracking": {
                          "enabled": false
                        },
                        "tags": {
                          "enabled": false
                        },
                        "time_estimates": {
                          "enabled": false
                        },
                        "checklists": {
                          "enabled": true
                        },
                        "custom_fields": {
                          "enabled": true
                        },
                        "remap_dependencies": {
                          "enabled": false
                        },
                        "dependency_warning": {
                          "enabled": false
                        },
                        "portfolios": {
                          "enabled": false
                        }
                      }
                    }
                  ]
                },
                "example": {
                  "id": "790",
                  "name": "Updated Space Name",
                  "private": false,
                  "statuses": [
                    {
                      "status": "to do",
                      "type": "open",
                      "orderindex": 0,
                      "color": "#d3d3d3"
                    },
                    {
                      "status": "complete",
                      "type": "closed",
                      "orderindex": 1,
                      "color": "#6bc950"
                    }
                  ],
                  "multiple_assignees": false,
                  "features": {
                    "due_dates": {
                      "enabled": false,
                      "start_date": false,
                      "remap_due_dates": false,
                      "remap_closed_due_date": false
                    },
                    "time_tracking": {
                      "enabled": false
                    },
                    "tags": {
                      "enabled": false
                    },
                    "time_estimates": {
                      "enabled": false
                    },
                    "checklists": {
                      "enabled": true
                    },
                    "custom_fields": {
                      "enabled": true
                    },
                    "remap_dependencies": {
                      "enabled": false
                    },
                    "dependency_warning": {
                      "enabled": false
                    },
                    "portfolios": {
                      "enabled": false
                    }
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
      "name": "Spaces"
    }
  ]
}
```