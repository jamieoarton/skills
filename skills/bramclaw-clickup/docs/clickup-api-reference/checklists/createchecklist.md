# Create Checklist

Add a new checklist to a task.

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
    "/v2/task/{task_id}/checklist": {
      "post": {
        "summary": "Create Checklist",
        "tags": [
          "Task Checklists"
        ],
        "description": "Add a new checklist to a task.",
        "operationId": "CreateChecklist",
        "parameters": [
          {
            "name": "task_id",
            "in": "path",
            "description": "",
            "required": true,
            "style": "simple",
            "schema": {
              "type": "string",
              "examples": [
                "9hz"
              ]
            }
          },
          {
            "name": "custom_task_ids",
            "in": "query",
            "description": "If you want to reference a task by it's custom task id, this value must be `true`.",
            "style": "form",
            "explode": true,
            "schema": {
              "type": "boolean",
              "examples": [
                true
              ]
            }
          },
          {
            "name": "team_id",
            "in": "query",
            "description": "When the `custom_task_ids` parameter is set to `true`, the Workspace ID must be provided using the `team_id` parameter.\n \\\nFor example: `custom_task_ids=true&team_id=123`.",
            "style": "form",
            "explode": true,
            "schema": {
              "type": "number",
              "contentEncoding": "double",
              "examples": [
                123
              ]
            }
          }
        ],
        "requestBody": {
          "description": "",
          "content": {
            "application/json": {
              "schema": {
                "title": "CreateChecklistrequest",
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
                    "name": "Checklist"
                  }
                ]
              },
              "example": {
                "name": "Checklist"
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
                  "title": "CreateChecklistresponse",
                  "required": [
                    "checklist"
                  ],
                  "type": "object",
                  "properties": {
                    "checklist": {
                      "title": "Checklist",
                      "required": [
                        "id",
                        "task_id",
                        "name",
                        "orderindex",
                        "resolved",
                        "unresolved",
                        "items"
                      ],
                      "type": "object",
                      "properties": {
                        "id": {
                          "type": "string"
                        },
                        "task_id": {
                          "type": "string"
                        },
                        "name": {
                          "type": "string"
                        },
                        "orderindex": {
                          "type": "integer",
                          "contentEncoding": "int32"
                        },
                        "resolved": {
                          "type": "integer",
                          "contentEncoding": "int32"
                        },
                        "unresolved": {
                          "type": "integer",
                          "contentEncoding": "int32"
                        },
                        "items": {
                          "type": "array",
                          "items": {
                            "type": "string"
                          },
                          "description": ""
                        }
                      },
                      "examples": [
                        {
                          "id": "b955c4dc-b8a8-48d8-a0c6-b4200788a683",
                          "task_id": "9hz",
                          "name": "Checklist",
                          "orderindex": 0,
                          "resolved": 0,
                          "unresolved": 0,
                          "items": []
                        }
                      ]
                    }
                  },
                  "examples": [
                    {
                      "checklist": {
                        "id": "b955c4dc-b8a8-48d8-a0c6-b4200788a683",
                        "task_id": "9hz",
                        "name": "Checklist",
                        "orderindex": 0,
                        "resolved": 0,
                        "unresolved": 0,
                        "items": []
                      }
                    }
                  ]
                },
                "example": {
                  "checklist": {
                    "id": "b955c4dc-b8a8-48d8-a0c6-b4200788a683",
                    "task_id": "9hz",
                    "name": "Checklist",
                    "orderindex": 0,
                    "resolved": 0,
                    "unresolved": 0,
                    "items": []
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
      "name": "Task Checklists"
    }
  ]
}
```